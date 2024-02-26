import numpy as np
import torch.nn as nn
import torch
import torch.nn.functional as F

class MLP(nn.Module):
    """
    Linear Embedding: 
    """
    def __init__(self, input_dim=2048, embed_dim=768):
        super().__init__()
        self.proj = nn.Linear(input_dim, embed_dim)

    def forward(self, x):
        x = x.flatten(2).transpose(1, 2)
        x = self.proj(x)
        return x

class Part2(nn.Module):
    def __init__(self,
                 in_channels=[64, 128, 320, 512],
                 num_classes=1,
                 dropout_ratio=0.1,
                 norm_layer=nn.BatchNorm2d,
                 embed_dim=768,
                 align_corners=False):
        
        super(Part2, self).__init__()
        self.num_classes = num_classes
        self.dropout_ratio = dropout_ratio
        self.align_corners = align_corners
        
        self.in_channels = in_channels
        
        if dropout_ratio > 0:
            self.dropout = nn.Dropout2d(dropout_ratio)
        else:
            self.dropout = None

        c1_in_channels, c2_in_channels, c3_in_channels, c4_in_channels = self.in_channels

        embedding_dim = embed_dim
        self.linear_c4 = MLP(input_dim=c4_in_channels, embed_dim=embedding_dim)
        self.linear_c3 = MLP(input_dim=c3_in_channels+embedding_dim, embed_dim=embedding_dim)
        self.linear_c2 = MLP(input_dim=c2_in_channels+embedding_dim, embed_dim=embedding_dim)
        self.linear_c1 = MLP(input_dim=c1_in_channels+embedding_dim, embed_dim=embedding_dim)
        
        self.linear_fuse = nn.Sequential(
                            nn.Conv2d(in_channels=embedding_dim*4, out_channels=embedding_dim, kernel_size=1),
                            norm_layer(embedding_dim),
                            nn.ReLU(inplace=True)
                            )
                            
        self.linear_pred = nn.Conv2d(embedding_dim, self.num_classes, kernel_size=1)
       
    def forward(self, inputs):
        c1, c2, c3, c4 = inputs
        n, _, h, w = c4.shape
        _c4 = self.linear_c4(c4).permute(0,2,1).reshape(n, -1, c4.shape[2], c4.shape[3])
        _c42 = F.interpolate(_c4, size=c3.size()[2:],mode='bilinear',align_corners=self.align_corners) #torch.Size([4, 768, 16, 16])

        c3_ = torch.cat((_c42,c3),dim=1)
        _c3 = self.linear_c3(c3_).permute(0,2,1).reshape(n, -1, c3.shape[2], c3.shape[3])
        _c3 = F.interpolate(_c3, size=c2.size()[2:],mode='bilinear',align_corners=self.align_corners)

        c2_ = torch.cat((_c3,c2),dim=1)
        _c2 = self.linear_c2(c2_).permute(0,2,1).reshape(n, -1, c2.shape[2], c2.shape[3])
        _c2 = F.interpolate(_c2, size=c1.size()[2:],mode='bilinear',align_corners=self.align_corners)
        
        c1_ = torch.cat((_c2,c1),dim=1)
        _c1 = self.linear_c1(c1_).permute(0,2,1).reshape(n, -1, c1.shape[2], c1.shape[3])
        #_c = self.linear_fuse(torch.cat([_c4, _c3, _c2, _c1], dim=1))
        x = self.dropout(_c1)
        x = self.linear_pred(x)
        return x

        