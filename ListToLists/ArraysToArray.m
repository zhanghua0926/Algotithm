//
//  ArraysToArray.m
//  TestDemo
//
//  Created by Eric on 2019/7/28.
//  Copyright © 2019 Eric. All rights reserved.
//

#import "ArraysToArray.h"

@implementation ArraysToArray

- (NSMutableArray *)arraysToArray:(NSMutableArray *)arr {
    NSMutableArray *result = [[NSMutableArray alloc] init];
    for (int i = 0; i < arr.count; i++) {
        if ([arr[i] isKindOfClass:[NSArray class]]) {
            result = [self arraysToArray:arr[i]];
        } else {
            [result addObject:arr[i]];
        }
    }
    
    return result;
}

@end
