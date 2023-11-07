import { Params } from "react-router-dom"

export interface ParamsProp {
    params: Params,
}

export interface UnitPlatform {
    namePlatform: string;
    percentage: string;
}

export interface listItemsCashback {
    bestPlatform: UnitPlatform[];
    evenPlatform: UnitPlatform[];
    worstPlatform: UnitPlatform[];
    platformNoCashbackPercentage: UnitPlatform[];
}