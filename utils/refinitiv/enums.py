from enum import Enum


class RefinitivField(Enum):
    pass


class EndOfDayField(RefinitivField):
    AdvancingIssues = "Advancing Issues"
    AdvancingVolume = "Advancing Volume"
    AlternateClose = "Alternate Close"
    Ask = "Ask"
    AssetID = "Asset ID"
    AssetStatus = "Asset Status"
    AssetStatusDescription = "Asset Status Description"
    AssetSubType = "Asset SubType"
    AssetSubTypeDescription = "Asset SubType Description"
    AssetType = "Asset Type"
    AssetTypeDescription = "Asset Type Description"
    Assets = "Assets"
    AverageMaturity = "Average Maturity"
    AverageofBidandAsk = "Average of Bid and Ask"
    BenchmarkPrice = "Benchmark Price"
    Bid = "Bid"
    BlockTrades = "Block Trades"
    BlockVolume = "Block Volume"
    CapitalGain = "Capital Gain"
    CloseYield = "Close Yield"
    CountryofIncorporation = "Country of Incorporation"
    CountryofIncorporationDescription = "Country of Incorporation Description"
    CRAAverageDailyTurnover = "CRA Average Daily Turnover"
    CRAAverageDailyTurnoverCurrencyCode = "CRA Average Daily Turnover Currency Code"
    CRAAverageValueofOrdersExecuted = "CRA Average Value of Orders Executed"
    CRAAverageValueofOrdersExecutedCurrencyCode = "CRA Average Value of Orders Executed Currency Code"
    CRAFreeFloat = "CRA Free Float"
    CRAFreeFloatCurrencyCode = "CRA Free Float Currency Code"
    CRAORGID = "CRA ORGID"
    CurrencyCode = "Currency Code"
    CurrencyCodeDescription = "Currency Code Description"
    CUSIP = "CUSIP"
    DecliningIssues = "Declining Issues"
    DecliningVolume = "Declining Volume"
    EligibleAccumulatedVolume = "Eligible Accumulated Volume"
    ESMAAverageDailyTurnover = "ESMA Average Daily Turnover"
    ESMAAverageDailyTurnoverCurrencyCode = "ESMA Average Daily Turnover Currency Code"
    ESMAAverageValueofOrdersExecuted = "ESMA Average Value of Orders Executed"
    ESMAAverageValueofOrdersExecutedCurrencyCode = "ESMA Average Value of Orders Executed Currency Code"
    ESMAFreeFloat = "ESMA Free Float"
    ESMAFreeFloatCurrencyCode = "ESMA Free Float Currency Code"
    ESMAMostRelevantMarket = "ESMA Most Relevant Market"
    ESMAStandardMarketSize = "ESMA Standard Market Size"
    ESMAStandardMarketSizeCurrencyCode = "ESMA Standard Market Size Currency Code"
    ExchangeCode = "Exchange Code"
    ExchangeDescription = "Exchange Description"
    ExpirationDate = "Expiration Date"
    FileCode = "File Code"
    Fixing = "Fixing"
    FloorVolume = "Floor Volume"
    Footnote = "Footnote"
    GICSIndustryCode = "GICS Industry Code"
    GICSIndustryCodeDescription = "GICS Industry Code Description"
    GICSIndustryDescriptionCode = "GICS Industry Description Code"
    GICSIndustryDescriptionCodeDescription = "GICS Industry Description Code Description"
    GICSIndustryGroupCode = "GICS Industry Group Code"
    GICSIndustryGroupCodeDescription = "GICS Industry Group Code Description"
    GICSSectorCode = "GICS Sector Code"
    GICSSectorCodeDescription = "GICS Sector Code Description"
    High = "High"
    HighYield = "High Yield"
    ImpliedVolatility = "Implied Volatility"
    InstrumentID = "Instrument ID"
    InstrumentIDType = "Instrument ID Type"
    InverseRateMarker = "Inverse Rate Marker"
    ISIN = "ISIN"
    IssuePermID = "Issue PermID"
    IssuerName = "Issuer Name"
    IssuerOrgID = "Issuer OrgID"
    IssuerPermID = "Issuer PermID"
    Last = "Last"
    LastTradingDay = "Last Trading Day"
    LotSize = "Lot Size"
    LotUnits = "Lot Units"
    Low = "Low"
    LowYield = "Low Yield"
    MalaysiaCode = "Malaysia Code"
    MarketMIC = "Market MIC"
    MarketVWAP = "Market VWAP"
    MIC = "MIC"
    MIFIDIndicator = "MIFID Indicator"
    MIFIDIndicatorDescription = "MIFID Indicator Description"
    NetAssetValue = "Net Asset Value"
    NewHighs = "New Highs"
    NewLows = "New Lows"
    NumberofPriceMoves = "Number of Price Moves"
    OffBookVolume = "Off Book Volume"
    OffFloorVolume = "Off Floor Volume"
    Offer = "Offer"
    OfficialHigh = "Official High"
    OfficialLow = "Official Low"
    OnFloorVolume = "On Floor Volume"
    Open = "Open"
    Open2 = "Open 2"
    OpenInterest = "Open Interest"
    OpenRangeType = "Open Range Type"
    OpenYield = "Open Yield"
    OPOL = "OPOL"
    PECode = "PE Code"
    PERatio = "PE Ratio"
    PILC = "PILC"
    PriceMovements = "Price Movements"
    PrimaryExecutionVenue = "Primary Execution Venue"
    PrimaryReferenceMarketQuote = "Primary Reference Market Quote"
    PutCallFlag = "Put Call Flag"
    QuoteID = "Quote ID"
    QuotePermID = "Quote PermID"
    RBSSCode = "RBSS Code"
    RBSSCodeDescription = "RBSS Code Description"
    RCPID = "RCP ID"
    ReferenceCompany = "Reference Company"
    ReutersEditorialRIC = "Reuters Editorial RIC"
    RIC = "RIC"
    RICRoot = "RIC Root"
    RoundLotSize = "Round Lot Size"
    SecurityDescription = "Security Description"
    SecurityLongDescription = "Security Long Description"
    SEDOL = "SEDOL"
    SettlementPrice = "Settlement Price"
    SevenDayCompoundedYield = "Seven Day Compounded Yield"
    SevenDayYield = "Seven Day Yield"
    SICC = "SICC"
    Sicovam = "Sicovam"
    ThomsonReutersClassificationScheme = "Thomson Reuters Classification Scheme"
    ThomsonReutersClassificationSchemeDescription = "Thomson Reuters Classification Scheme Description"
    Ticker = "Ticker"
    TotalIssues = "Total Issues"
    TotalVolume2 = "Total Volume 2"
    TradeDate = "Trade Date"
    TradingStatus = "Trading Status"
    TradingSymbol = "Trading Symbol"
    TRBCActivityCode = "TRBC Activity Code"
    TRBCActivityCodeDescription = "TRBC Activity Code Description"
    TRBCBusinessSectorCode = "TRBC Business Sector Code"
    TRBCBusinessSectorCodeDescription = "TRBC Business Sector Code Description"
    TRBCEconomicSectorCode = "TRBC Economic Sector Code"
    TRBCEconomicSectorCodeDescription = "TRBC Economic Sector Code Description"
    TRBCIndustryCode = "TRBC Industry Code"
    TRBCIndustryCodeDescription = "TRBC Industry Code Description"
    TRBCIndustryGroupCode = "TRBC Industry Group Code"
    TRBCIndustryGroupCodeDescription = "TRBC Industry Group Code Description"
    Turnover = "Turnover"
    UnchangedIssues = "Unchanged Issues"
    UnchangedVolume = "Unchanged Volume"
    UnderlyingRIC = "Underlying RIC"
    UniversalAskPrice = "Universal Ask Price"
    UniversalBidPrice = "Universal Bid Price"
    UniversalClosePrice = "Universal Close Price"
    UsageInstrumentSubType = "Usage Instrument SubType"
    UsageInstrumentType = "Usage Instrument Type"
    UserDefinedIdentifier = "User Defined Identifier"
    UserDefinedIdentifier2 = "User Defined Identifier2"
    UserDefinedIdentifier3 = "User Defined Identifier3"
    UserDefinedIdentifier4 = "User Defined Identifier4"
    UserDefinedIdentifier5 = "User Defined Identifier5"
    UserDefinedIdentifier6 = "User Defined Identifier6"
    Valoren = "Valoren"
    Volume = "Volume"
    VWAP = "VWAP"
    Wertpapier = "Wertpapier"
    Yield = "Yield"


class IntradayField(RefinitivField):
    CloseAsk = "Close Ask"
    CloseAskYield = "Close Ask Yield"
    CloseBid = "Close Bid"
    CloseBidYield = "Close Bid Yield"
    CloseDiscountFactor = "Close Discount Factor"
    CloseYield = "Close Yield"
    CloseZeroYield = "Close Zero Yield"
    High = "High"
    HighAsk = "High Ask"
    HighAskYield = "High Ask Yield"
    HighBid = "High Bid"
    HighBidYield = "High Bid Yield"
    HighDiscountFactor = "High Discount Factor"
    HighYield = "High Yield"
    HighZeroYield = "High Zero Yield"
    Last = "Last"
    Low = "Low"
    LowAsk = "Low Ask"
    LowAskYield = "Low Ask Yield"
    LowBid = "Low Bid"
    LowBidYield = "Low Bid Yield"
    LowDiscountFactor = "Low Discount Factor"
    LowYield = "Low Yield"
    LowZeroYield = "Low Zero Yield"
    NumAskYields = "No. Ask Yields"
    NumAsks = "No. Asks"
    NumBidYields = "No. Bid Yields"
    NumBids = "No. Bids"
    NumDiscountFactors = "No. Discount Factors"
    NumTrades = "No. Trades"
    NumYields = "No. Yields"
    NumZeroYields = "No. Zero Yields"
    Open = "Open"
    OpenAsk = "Open Ask"
    OpenAskYield = "Open Ask Yield"
    OpenBid = "Open Bid"
    OpenBidYield = "Open Bid Yield"
    OpenDiscountFactor = "Open Discount Factor"
    OpenYield = "Open Yield"
    OpenZeroYield = "Open Zero Yield"
    Volume = "Volume"


class MarketDepthField(RefinitivField):
    AskPrice = "Ask Price"
    AskSize = "Ask Size"
    BidPrice = "Bid Price"
    BidSize = "Bid Size"
    NumberofBuyers = "Number of Buyers"
    NumberofSellers = "Number of Sellers"


class TimeAndSalesField(RefinitivField):
    AuctionExchangeTime = "Auction - Exchange Time"
    AuctionPrice = "Auction - Price"
    AuctionQualifiers = "Auction - Qualifiers"
    AuctionSequenceNumber = "Auction - Sequence Number"
    AuctionVolume = "Auction - Volume"
    CorrectionAccumulatedVolume = "Correction - Accumulated Volume"
    CorrectionAskPrice = "Correction - Ask Price"
    CorrectionBidPrice = "Correction - Bid Price"
    CorrectionBuyerID = "Correction - Buyer ID"
    CorrectionExchangeTime = "Correction - Exchange Time"
    CorrectionExchangeContributorID = "Correction - Exchange/Contributor ID"
    CorrectionISIN = "Correction - ISIN"
    CorrectionMarketVWAP = "Correction - Market VWAP"
    CorrectionOrderbookVWAP = "Correction - Orderbook VWAP"
    CorrectionOriginalAccumulatedVolume = "Correction - Original Accumulated Volume"
    CorrectionOriginalBuyerID = "Correction - Original Buyer ID"
    CorrectionOriginalDate = "Correction - Original Date"
    CorrectionOriginalExchangeTime = "Correction - Original Exchange Time"
    CorrectionOriginalPrice = "Correction - Original Price"
    CorrectionOriginalPrimaryActivity = "Correction - Original Primary Activity"
    CorrectionOriginalRICofLastEligibleTrade = "Correction - Original RIC of Last Eligible Trade"
    CorrectionOriginalSellerID = "Correction - Original Seller ID"
    CorrectionOriginalSequenceNumber = "Correction - Original Sequence Number"
    CorrectionOriginalTradeSequenceNumber = "Correction - Original Trade Sequence Number"
    CorrectionOriginalUniqueTradeIdentification = "Correction - Original Unique Trade Identification"
    CorrectionOriginalVolume = "Correction - Original Volume"
    CorrectionOriginalYield = "Correction - Original Yield"
    CorrectionPERatio = "Correction - PE Ratio"
    CorrectionPrice = "Correction - Price"
    CorrectionPrimaryActivity = "Correction - Primary Activity"
    CorrectionQualifiers = "Correction - Qualifiers"
    CorrectionRICofLastEligibleTrade = "Correction - RIC of Last Eligible Trade"
    CorrectionSellerID = "Correction - Seller ID"
    CorrectionSequenceNumber = "Correction - Sequence Number"
    CorrectionTradeSequenceNumber = "Correction - Trade Sequence Number"
    CorrectionVolume = "Correction - Volume"
    CorrectionYield = "Correction - Yield"
    MarketConditionsQualifiers = "Market Conditions - Qualifiers"
    Quote1MBasisAssetSwapSpread = "Quote - 1M Basis Asset Swap Spread"
    Quote30DayATMIVCall = "Quote - 30 Day ATM IV Call"
    Quote30DayATMIVPut = "Quote - 30 Day ATM IV Put"
    Quote3MBasisAssetSwapSpread = "Quote - 3M Basis Asset Swap Spread"
    Quote60DayATMIVCall = "Quote - 60 Day ATM IV Call"
    Quote60DayATMIVPut = "Quote - 60 Day ATM IV Put"
    Quote6MBasisAssetSwapSpread = "Quote - 6M Basis Asset Swap Spread"
    Quote90DayATMIVCall = "Quote - 90 Day ATM IV Call"
    Quote90DayATMIVPut = "Quote - 90 Day ATM IV Put"
    QuoteAccumulatedAskOrder = "Quote - Accumulated Ask Order"
    QuoteAccumulatedAskOrderSize = "Quote - Accumulated Ask Order Size"
    QuoteAccumulatedBidOrder = "Quote - Accumulated Bid Order"
    QuoteAccumulatedBidOrderSize = "Quote - Accumulated Bid Order Size"
    QuoteAskCompoundYield = "Quote - Ask Compound Yield"
    QuoteAskDealerCount = "Quote - Ask Dealer Count"
    QuoteAskImpliedVolatility = "Quote - Ask Implied Volatility"
    QuoteAskMarketMakerID = "Quote - Ask Market Maker ID"
    QuoteAskPrice = "Quote - Ask Price"
    QuoteAskSize = "Quote - Ask Size"
    QuoteAskSpread = "Quote - Ask Spread"
    QuoteAskYield = "Quote - Ask Yield"
    QuoteAssetSwapSpread = "Quote - Asset Swap Spread"
    QuoteAssetSwapSpreadAsk = "Quote - Asset Swap Spread Ask"
    QuoteAssetSwapSpreadBid = "Quote - Asset Swap Spread Bid"
    QuoteBackgroundReference = "Quote - Background Reference"
    QuoteBaseCorrelation = "Quote - Base Correlation"
    QuoteBasisPointVolatilty = "Quote - Basis Point Volatilty"
    QuoteBenchPrice = "Quote - Bench Price"
    QuoteBenchmarkSpread = "Quote - Benchmark Spread"
    QuoteBenchmarkSpreadAsk = "Quote - Benchmark Spread Ask"
    QuoteBenchmarkSpreadBid = "Quote - Benchmark Spread Bid"
    QuoteBenchmarkYield = "Quote - Benchmark Yield"
    QuoteBidCompoundYield = "Quote - Bid Compound Yield"
    QuoteBidDealerCount = "Quote - Bid Dealer Count"
    QuoteBidImpliedVolatility = "Quote - Bid Implied Volatility"
    QuoteBidMarketMakerID = "Quote - Bid Market Maker ID"
    QuoteBidPrice = "Quote - Bid Price"
    QuoteBidSize = "Quote - Bid Size"
    QuoteBidSpread = "Quote - Bid Spread"
    QuoteBidTick = "Quote - Bid Tick"
    QuoteBidYield = "Quote - Bid Yield"
    QuoteBondFloor = "Quote - Bond Floor"
    QuoteBPV = "Quote - BPV"
    QuoteBreakevenInflation = "Quote - Breakeven Inflation"
    QuoteBuyerID = "Quote - Buyer ID"
    QuoteCapPremium = "Quote - Cap Premium"
    QuoteCarryRolldownTotal = "Quote - Carry Roll-down Total"
    QuoteCDSDollarValueOf1BasisPoint = "Quote - CDS Dollar Value Of 1 Basis Point"
    QuoteClosesttoMaturityCDSBasis = "Quote - Closest-to-Maturity CDS Basis"
    QuoteConstantMaturityYield = "Quote - Constant Maturity Yield"
    QuoteContributorLocationCode = "Quote - Contributor Location Code"
    QuoteConversionFactor = "Quote - Conversion Factor"
    QuoteConversionPremium = "Quote - Conversion Premium"
    QuoteConversionRatio = "Quote - Conversion Ratio"
    QuoteConvexity = "Quote - Convexity"
    QuoteConvexityBias = "Quote - Convexity Bias"
    QuoteCostofCarry = "Quote - Cost of Carry"
    QuoteCrack = "Quote - Crack"
    QuoteDate = "Quote - Date"
    QuoteDealingCode = "Quote - Dealing Code"
    QuoteDefaultProbability = "Quote - Default Probability"
    QuoteDelta = "Quote - Delta"
    QuoteDiscountAsk = "Quote - Discount Ask"
    QuoteDiscountBid = "Quote - Discount Bid"
    QuoteDiscountFactor = "Quote - Discount Factor"
    QuoteDiscountMargin = "Quote - Discount Margin"
    QuoteDiscountMarginAsk = "Quote - Discount Margin Ask"
    QuoteDiscountMarginBid = "Quote - Discount Margin Bid"
    QuoteDiscountRate = "Quote - Discount Rate"
    QuoteDisplayName = "Quote - Display Name"
    QuoteDuration = "Quote - Duration"
    QuoteEdge = "Quote - Edge"
    QuoteEffectiveConvexity = "Quote - Effective Convexity"
    QuoteEffectiveDuration = "Quote - Effective Duration"
    QuoteExchangeTime = "Quote - Exchange Time"
    QuoteExchangeContributorID = "Quote - Exchange/Contributor ID"
    QuoteFairPrice = "Quote - Fair Price"
    QuoteFairValueAccuracyMeasure = "Quote - Fair Value Accuracy Measure"
    QuoteFairValueConsistencyScore = "Quote - Fair Value Consistency Score"
    QuoteFairValueDV01 = "Quote - Fair Value DV01"
    QuoteFairValueSpread = "Quote - Fair Value Spread"
    QuoteFairValueYield = "Quote - Fair Value Yield"
    QuoteFarClearingPrice = "Quote - Far Clearing Price"
    QuoteFixedCoupon = "Quote - Fixed Coupon"
    QuoteFixingDate = "Quote - Fixing Date"
    QuoteFixingValue = "Quote - Fixing Value"
    QuoteFloorPremium = "Quote - Floor Premium"
    QuoteForecastAverageSwapPoints = "Quote - Forecast Average Swap Points"
    QuoteForecastHigh = "Quote - Forecast High"
    QuoteForecastLow = "Quote - Forecast Low"
    QuoteForecastMean = "Quote - Forecast Mean"
    QuoteForecastMedian = "Quote - Forecast Median"
    QuoteForecastStandardDeviation = "Quote - Forecast Standard Deviation"
    QuoteForwardFutureRisk = "Quote - Forward Future Risk"
    QuoteForwardOutrightAsk = "Quote - Forward Outright Ask"
    QuoteForwardOutrightBid = "Quote - Forward Outright Bid"
    QuoteForwardRate = "Quote - Forward Rate"
    QuoteFreightPrice = "Quote - Freight Price"
    QuoteFuturesBasis = "Quote - Futures Basis"
    QuoteFuturesRisk = "Quote - Futures Risk"
    QuoteGamma = "Quote - Gamma"
    QuoteGrossBasis = "Quote - Gross Basis"
    QuoteHaltReason = "Quote - Halt Reason"
    QuoteHedgeRatio = "Quote - Hedge Ratio"
    QuoteHigh = "Quote - High"
    QuoteHighYield = "Quote - High Yield"
    QuoteImbalanceActivityType = "Quote - Imbalance Activity Type"
    QuoteImbalanceQuantity = "Quote - Imbalance Quantity"
    QuoteImbalanceSide = "Quote - Imbalance Side"
    QuoteImbalanceVariationIndicator = "Quote - Imbalance Variation Indicator"
    QuoteImpliedCorrelation = "Quote - Implied Correlation"
    QuoteImpliedRepoRate = "Quote - Implied Repo Rate"
    QuoteImpliedVolatility = "Quote - Implied Volatility"
    QuoteImpliedYield = "Quote - Implied Yield"
    QuoteIndexSkew = "Quote - Index Skew"
    QuoteInterpolatedCDSBasis = "Quote - Interpolated CDS Basis"
    QuoteInterpolatedCDSSpread = "Quote - Interpolated CDS Spread"
    QuoteInvoicePrice = "Quote - Invoice Price"
    QuoteInvoiceSpread = "Quote - Invoice Spread"
    QuoteISIN = "Quote - ISIN"
    QuoteISMAAskYield = "Quote - ISMA Ask Yield"
    QuoteISMABidYield = "Quote - ISMA Bid Yield"
    QuoteLevelUpLevelDownIndicator = "Quote - Level-Up Level-Down Indicator"
    QuoteLow = "Quote - Low"
    QuoteLowYield = "Quote - Low Yield"
    QuoteLowerLimitPrice = "Quote - Lower Limit Price"
    QuoteMeanReversion = "Quote - Mean Reversion"
    QuoteMidPrice = "Quote - Mid Price"
    QuoteMidSpread = "Quote - Mid Spread"
    QuoteMidYield = "Quote - Mid Yield"
    QuoteModifiedDuration = "Quote - Modified Duration"
    QuoteNearClearingPrice = "Quote - Near Clearing Price"
    QuoteNetBasis = "Quote - Net Basis"
    QuoteNetChange = "Quote - Net Change"
    QuoteNumberofBuyers = "Quote - Number of Buyers"
    QuoteNumberofSellers = "Quote - Number of Sellers"
    QuoteOpen = "Quote - Open"
    QuoteOpenYield = "Quote - Open Yield"
    QuoteOptionAdjustedSpread = "Quote - Option Adjusted Spread"
    QuoteOptionAdjustedSpreadAsk = "Quote - Option Adjusted Spread Ask"
    QuoteOptionAdjustedSpreadBid = "Quote - Option Adjusted Spread Bid"
    QuotePairedQuantity = "Quote - Paired Quantity"
    QuoteParYield = "Quote - Par Yield"
    QuoteParity = "Quote - Parity"
    QuotePercentageDailyReturn = "Quote - Percentage Daily Return"
    QuotePremium = "Quote - Premium"
    QuotePresentValueofBasisPoint = "Quote - Present Value of Basis Point"
    QuotePrice = "Quote - Price"
    QuoteQualifiers = "Quote - Qualifiers"
    QuoteRealYieldAsk = "Quote - Real Yield Ask"
    QuoteRealYieldBid = "Quote - Real Yield Bid"
    QuoteRecoveryRate = "Quote - Recovery Rate"
    QuoteReferenceBondYield = "Quote - Reference Bond Yield"
    QuoteReferencePrice = "Quote - Reference Price"
    QuoteReserveVol = "Quote - Reserve Vol"
    QuoteRolldown = "Quote - Roll-down"
    QuoteRunningSpread = "Quote - Running Spread"
    QuoteSellerID = "Quote - Seller ID"
    QuoteSequenceNumber = "Quote - Sequence Number"
    QuoteShortRateVolatility = "Quote - Short Rate Volatility"
    QuoteShortSaleRestrictionIndicator = "Quote - Short Sale Restriction Indicator"
    QuoteSimpleMargin = "Quote - Simple Margin"
    QuoteSourceReference = "Quote - Source Reference"
    QuoteSovereignSpread = "Quote - Sovereign Spread"
    QuoteSpreadtoTreasury = "Quote - Spread to Treasury"
    QuoteStrike = "Quote - Strike"
    QuoteSwapPoint = "Quote - Swap Point"
    QuoteSwapPremium = "Quote - Swap Premium"
    QuoteSwapRate = "Quote - Swap Rate"
    QuoteSwapSpread = "Quote - Swap Spread"
    QuoteSwapSpreadAsk = "Quote - Swap Spread Ask"
    QuoteSwapSpreadBid = "Quote - Swap Spread Bid"
    QuoteSwapYield = "Quote - Swap Yield"
    QuoteTheoreticalPrice = "Quote - Theoretical Price"
    QuoteTheoreticalPriceAsk = "Quote - Theoretical Price Ask"
    QuoteTheoreticalPriceBid = "Quote - Theoretical Price Bid"
    QuoteTheoreticalPriceMid = "Quote - Theoretical Price Mid"
    QuoteTheoreticalSpreadAsk = "Quote - Theoretical Spread Ask"
    QuoteTheoreticalSpreadBid = "Quote - Theoretical Spread Bid"
    QuoteTheoreticalSpreadMid = "Quote - Theoretical Spread Mid"
    QuoteTheta = "Quote - Theta"
    QuoteTop = "Quote - Top"
    QuoteTradingStatus = "Quote - Trading Status"
    QuoteUniqueQuoteIdentification = "Quote - Unique Quote Identification"
    QuoteUpperLimitPrice = "Quote - Upper Limit Price"
    QuoteVolatility = "Quote - Volatility"
    QuoteVolume = "Quote - Volume"
    QuoteYield = "Quote - Yield"
    QuoteYieldToCall = "Quote - Yield To Call"
    QuoteYieldtoMaturity = "Quote - Yield to Maturity"
    QuoteYieldtoMaturityAsk = "Quote - Yield to Maturity Ask"
    QuoteYieldtoMaturityBid = "Quote - Yield to Maturity Bid"
    QuoteYieldToPut = "Quote - Yield To Put"
    QuoteYTB = "Quote - YTB"
    QuoteYTW = "Quote - YTW"
    QuoteZSpread = "Quote - Z Spread"
    QuoteZeroYield = "Quote - Zero Yield"
    ReferenceChangeChangeType = "Reference Change - Change Type"
    ReferenceChangeNewValue = "Reference Change - New Value"
    ReferenceChangeOldValue = "Reference Change - Old Value"
    SettlementPriceDate = "Settlement Price - Date"
    SettlementPricePrice = "Settlement Price - Price"
    SymbologyChangeChangeType = "SymbologyMessageHandler Change - Change Type"
    SymbologyChangeNewValue = "SymbologyMessageHandler Change - New Value"
    SymbologyChangeOldValue = "SymbologyMessageHandler Change - Old Value"
    Trade30DayATMIVCall = "Trade - 30 Day ATM IV Call"
    Trade30DayATMIVPut = "Trade - 30 Day ATM IV Put"
    Trade60DayATMIVCall = "Trade - 60 Day ATM IV Call"
    Trade60DayATMIVPut = "Trade - 60 Day ATM IV Put"
    Trade90DayATMIVCall = "Trade - 90 Day ATM IV Call"
    Trade90DayATMIVPut = "Trade - 90 Day ATM IV Put"
    TradeAccumulatedAskOrder = "Trade - Accumulated Ask Order"
    TradeAccumulatedAskOrderSize = "Trade - Accumulated Ask Order Size"
    TradeAccumulatedBidOrder = "Trade - Accumulated Bid Order"
    TradeAccumulatedBidOrderSize = "Trade - Accumulated Bid Order Size"
    TradeAccumulatedVolume = "Trade - Accumulated Volume"
    TradeActual = "Trade - Actual"
    TradeAdvancingIssues = "Trade - Advancing Issues"
    TradeAdvancingMoves = "Trade - Advancing Moves"
    TradeAdvancingVolume = "Trade - Advancing Volume"
    TradeAggressiveOrderCondition = "Trade - Aggressive Order Condition"
    TradeAskPrice = "Trade - Ask Price"
    TradeAskSize = "Trade - Ask Size"
    TradeAskYield = "Trade - Ask Yield"
    TradeAveragePrice = "Trade - Average Price"
    TradeBackgroundReference = "Trade - Background Reference"
    TradeBenchPrice = "Trade - Bench Price"
    TradeBidPrice = "Trade - Bid Price"
    TradeBidSize = "Trade - Bid Size"
    TradeBidYield = "Trade - Bid Yield"
    TradeBlockTrade = "Trade - Block Trade"
    TradeBuyerID = "Trade - Buyer ID"
    TradeCategorizationofTrades = "Trade - Categorization of Trades"
    TradeChangedMarket = "Trade - Changed Market"
    TradeCommodityBasis = "Trade - Commodity Basis"
    TradeCompoundYield = "Trade - Compound Yield"
    TradeContributorLocationCode = "Trade - Contributor Location Code"
    TradeCrack = "Trade - Crack"
    TradeDailyQuotaRemainingBalance = "Trade - Daily Quota Remaining Balance"
    TradeDate = "Trade - Date"
    TradeDealingCode = "Trade - Dealing Code"
    TradeDecliningIssues = "Trade - Declining Issues"
    TradeDecliningMoves = "Trade - Declining Moves"
    TradeDecliningVolume = "Trade - Declining Volume"
    TradeDisplayName = "Trade - Display Name"
    TradeEnergyNetback = "Trade - Energy Netback"
    TradeEnergySwing = "Trade - Energy Swing"
    TradeEnergyVariance = "Trade - Energy Variance"
    TradeExchangeForPhysicalVolume = "Trade - Exchange For Physical Volume"
    TradeExchangeForSwapsVolume = "Trade - Exchange For Swaps Volume"
    TradeExchangeTime = "Trade - Exchange Time"
    TradeExchangeContributorID = "Trade - Exchange/Contributor ID"
    TradeFairValue = "Trade - Fair Value"
    TradeFairValueVolume = "Trade - Fair Value Volume"
    TradeFinalNAV = "Trade - Final NAV"
    TradeFinalPhysicalNotification = "Trade - Final Physical Notification"
    TradeFlows = "Trade - Flows"
    TradeForecast = "Trade - Forecast"
    TradeForecastHigh = "Trade - Forecast High"
    TradeForecastLow = "Trade - Forecast Low"
    TradeFreightPrice = "Trade - Freight Price"
    TradeHaltReason = "Trade - Halt Reason"
    TradeHigh = "Trade - High"
    TradeImpliedVolatility = "Trade - Implied Volatility"
    TradeIndicativeAuctionPrice = "Trade - Indicative Auction Price"
    TradeIndicativeAuctionVolume = "Trade - Indicative Auction Volume"
    TradeInstrumentDescription = "Trade - Instrument Description"
    TradeISIN = "Trade - ISIN"
    TradeLevelUpLevelDownIndicator = "Trade - Level-Up Level-Down Indicator"
    TradeLow = "Trade - Low"
    TradeLowerLimitPrice = "Trade - Lower Limit Price"
    TradeMarketVolatility = "Trade - Market Volatility"
    TradeMarketVWAP = "Trade - Market VWAP"
    TradeMaximumExportLimit = "Trade - Maximum Export Limit"
    TradeMaximumImportLimit = "Trade - Maximum Import Limit"
    TradeMidPrice = "Trade - Mid Price"
    TradeMMTClassification = "Trade - MMT Classification"
    TradeNetChange = "Trade - Net Change"
    TradeNewHighs = "Trade - New Highs"
    TradeNewLows = "Trade - New Lows"
    TradeNumberofForecasts = "Trade - Number of Forecasts"
    TradeNumberofTrades = "Trade - Number of Trades"
    TradeOddLotTradePrice = "Trade - Odd-Lot Trade Price"
    TradeOddLotTradeTurnover = "Trade - Odd-Lot Trade Turnover"
    TradeOddLotTradeVolume = "Trade - Odd-Lot Trade Volume"
    TradeOffer = "Trade - Offer"
    TradeOpen = "Trade - Open"
    TradeOpenInterest = "Trade - Open Interest"
    TradeOrderbookVWAP = "Trade - Orderbook VWAP"
    TradeOriginalPrice = "Trade - Original Price"
    TradeOriginalVolume = "Trade - Original Volume"
    TradePERatio = "Trade - PE Ratio"
    TradePercentChange = "Trade - Percent Change"
    TradePremium = "Trade - Premium"
    TradePrice = "Trade - Price"
    TradePrimaryActivity = "Trade - Primary Activity"
    TradePrior = "Trade - Prior"
    TradeQualifiers = "Trade - Qualifiers"
    TradeQuscntPhysicalNotification = "Trade - Quscnt Physical Notification"
    TradeRefineryMarginCrack = "Trade - Refinery Margin Crack"
    TradeRefineryMarginTop = "Trade - Refinery Margin Top"
    TradeRevised = "Trade - Revised"
    TradeRICofLastEligibleTrade = "Trade - RIC of Last Eligible Trade"
    TradeSeasonalNormalDemand = "Trade - Seasonal Normal Demand"
    TradeSellerID = "Trade - Seller ID"
    TradeSequenceNumber = "Trade - Sequence Number"
    TradeShortSaleRestrictionIndicator = "Trade - Short Sale Restriction Indicator"
    TradeSourceReference = "Trade - Source Reference"
    TradeStrike = "Trade - Strike"
    TradeStrongMarket = "Trade - Strong Market"
    TradeTickDirection = "Trade - Tick Direction"
    TradeTop = "Trade - Top"
    TradeTotalBuyValue = "Trade - Total Buy Value"
    TradeTotalBuyVolume = "Trade - Total Buy Volume"
    TradeTotalDemand = "Trade - Total Demand"
    TradeTotalIssues = "Trade - Total Issues"
    TradeTotalMoves = "Trade - Total Moves"
    TradeTotalSellValue = "Trade - Total Sell Value"
    TradeTotalSellVolume = "Trade - Total Sell Volume"
    TradeTotalVolume = "Trade - Total Volume"
    TradeTradePriceCurrency = "Trade - Trade Price Currency"
    TradeTradeSequenceNumber = "Trade - Trade Sequence Number"
    TradeTradeYield = "Trade - Trade Yield"
    TradeTradingStatus = "Trade - Trading Status"
    TradeTurnover = "Trade - Turnover"
    TradeUnchangedIssues = "Trade - Unchanged Issues"
    TradeUnchangedMoves = "Trade - Unchanged Moves"
    TradeUnchangedVolume = "Trade - Unchanged Volume"
    TradeUniqueTradeIdentification = "Trade - Unique Trade Identification"
    TradeUpperLimitPrice = "Trade - Upper Limit Price"
    TradeVolatility = "Trade - Volatility"
    TradeVolume = "Trade - Volume"
    TradeWeakMarket = "Trade - Weak Market"
    TradeYield = "Trade - Yield"


class SummaryInterval(Enum):
    ONE_HOUR = "OneHour"


class TemplateType(Enum):
    TIME_AND_SALES = "TickHistoryTimeAndSales"
    MARKET_DEPTH = "TickHistoryMarketDepth"
    INTRADAY_BARS = "TickHistoryIntradaySummaries"
    END_OF_DAY = "ElektronTimeseries"


class RequestType(Enum):
    TIME_AND_SALES = "TickHistoryTimeAndSalesExtractionRequest"
    MARKET_DEPTH = "TickHistoryMarketDepthExtractionRequest"
    INTRADAY_BARS = "TickHistoryIntradaySummariesExtractionRequest"
    END_OF_DAY = "ElektronTimeseriesExtractionRequest"

class SearchType(Enum):
    INSTRUMENT = "AllInstrumentSearchRequest"


class QuotaCategoryCode(Enum):
    Cash = "Cash"
    Futures = "Futures"


class AssetClass(Enum):
    Cash = "Cash"
    Futures = "Futures"

class InstrumentTypeGroup(Enum):
    CollatetizedMortgageObligations = "CollatetizedMortgageObligations"  # Collaterized Mortgage Obligations (CMO)
    Commodities = "Commodities"  # Commodities
    Equities = "Equities"  # Equities
    Funds = "Funds"  # Funds
    FuturesAndOptions = "FuturesAndOptions"  # Futures and Options
    GovCorp = "GovCorp"  # Gov/Corp
    Money = "Money"  # Money
    MortgageBackedSecurities = "MortgageBackedSecurities"  # Mortgage Backed Securities (MBS)
    Municipals = "Municipals"  # US Municipals

class IdentifierType(Enum):
    Ric = "Ric"
    ChainRic = "ChainRIC"
