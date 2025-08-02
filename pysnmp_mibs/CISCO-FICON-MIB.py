_BN='cficonDefaultPortBlockGroup'
_BM='cficonPortMapGroup'
_BL='cficonPortInfoChange'
_BK='cficonDefaultPortBlock'
_BJ='cficonInterfaceSwapNextIndex'
_BI='cficonSwapInterfaceEntryStatus'
_BH='cficonSwapInterfaceSystemError'
_BG='cficonSwapInterfaceFailReason'
_BF='cficonSwapInterfaceActionStatus'
_BE='cficonSwapInterfaceIndexSecond'
_BD='cficonSwapInterfaceIndexFirst'
_BC='cficonRlirErlRegType'
_BB='cficonLogicReservedPN'
_BA='cficonSlotReservedPN'
_B9='cficonPortMapObj'
_B8='cficonPortMapMax'
_B7='cficonPortMap6'
_B6='cficonPortMap5'
_B5='cficonPortMap4'
_B4='cficonPortMap3'
_B3='cficonPortMap2'
_B2='cficonPortMap1'
_B1='cficonAutoSaveState'
_B0='cficonCopyEntryRowStatus'
_A_='cficonCopyFailReason'
_Az='cficonCopyState'
_Ay='cficonCfgFileCupName'
_Ax='cficonLinkIncidentClear'
_Aw='cficonLinkIncidentTime'
_Av='cficonLinkIncident'
_Au='cficonShowPorts'
_At='cfStatsErrorSummary'
_As='cfStatsInvalidOrderSets'
_Ar='cfStatsDispErrsOutOfFrame'
_Aq='cfStatsEOFErrs'
_Ap='cfStatsDispErrorsInFrame'
_Ao='cfStatsFramePacingTime'
_An='cficonDirHistPortNumbers'
_Am='portAddress'
_Al='cficonPortAddrPortNumber'
_Ak='cficonPortIfIndex'
_Aj='cficonCfgFileCmdErrorString'
_Ai='cficonCfgFileCmdStatus'
_Ah='cficonCfgFileRowStatus'
_Ag='cficonCfgFileCmd'
_Af='cficonCfgFileLastUpdated'
_Ae='cficonCfgFileStatus'
_Ad='cficonCfgFileDescr'
_Ac='cficonRunCfgStatus'
_Ab='cficonRunCfgPortId'
_Aa='cficonRunCfgSerialNumber'
_AZ='cficonRunCfgPlantOfMfg'
_AY='cficonRunCfgManufacturer'
_AX='cficonRunCfgModelNumber'
_AW='cficonRunCfgTypeNumber'
_AV='cficonRunCfgProhibitPrtNums'
_AU='cficonPortRunCfgName'
_AT='cficonPortRunCfgBlock'
_AS='cficonProhibitPortNumbers'
_AR='cficonPortName'
_AQ='cficonPortBlock'
_AP='cficonVsanSerialNum'
_AO='cficonVsanFiconState'
_AN='cficonVsanEntryStatus'
_AM='cficonVsanClearAllegience'
_AL='cficonSetHostTimeControl'
_AK='cficonVsanCupName'
_AJ='cficonVsanHostOrDefaultTime'
_AI='cficonVsanTime'
_AH='cficonVsanDeviceAllegience'
_AG='cficonVsanUserAlertMode'
_AF='cficonVsanKeyCounter'
_AE='cficonVsanCharSet'
_AD='cficonVsanCodePage'
_AC='cficonVsanEnableCup'
_AB='cficonVsanAutoSavePortAddrCfg'
_AA='cficonVsanSnmpControl'
_A9='cficonVsanHostControlClkAlrtMode'
_A8='cficonVsanHostControlSwOffline'
_A7='cficonVsanHostControl'
_A6='cficonSwapPortEntryStatus'
_A5='cficonSwapPortNumberSecond'
_A4='cficonSwapPortNumberFirst'
_A3='cficonInterfaceSwapIndex'
_A2='cficonRlirErlFormat'
_A1='cficonRlirErlFcId'
_A0='cficonSlotIndex'
_z='cficonPortMapIndex'
_y='cficonConfigCopyIndex'
_x='cficonDirHistKeyCounter'
_w='portAddrPortNumber'
_v='cficonPortAddrPortAddr'
_u='cficonPortNumber'
_t='failed'
_s='inProgress'
_r='cficonPortRunCfgAddr'
_q='cficonPortAddr'
_p='unlocked'
_o='cficonPortSwapIndex'
_n='cficonInterfaceSwapGroup'
_m='cficonRunCfgUnitType'
_l='success'
_k='Unsigned32'
_j='cficonRlirErlGroup'
_i='cficonReservedPortNumGroup'
_h='cficonPortMapGroupRev1'
_g='cficonCfgFilename'
_f='ifIndex'
_e='IF-MIB'
_d='cficonNotificationGroup'
_c='cficonAutoSaveStateGroup'
_b='cficonConfigCopyGroup'
_a='cficonCfgFileCupNameGroup'
_Z='cficonLinkIncidentGroup'
_Y='cifconShowPortGroup'
_X='cficonStatsGroup'
_W='cficonDirHistGroup'
_V='cficonPortNumAddrGroup'
_U='cficonPortAddrNumGroup'
_T='cficonPortNumIfGroup'
_S='cficonCfgFileGroup'
_R='cficonPortRunCfgGroup'
_Q='cficonPortGroup'
_P='cficonVsanGroup'
_O='cficonPortSwapGroup'
_N='SnmpAdminString'
_M='DisplayString'
_L='vsanIndex'
_K='CISCO-VSAN-MIB'
_J='deprecated'
_I='TruthValue'
_H='OctetString'
_G='read-write'
_F='not-accessible'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-FICON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddressId,=mibBuilder.importSymbols('CISCO-ST-TC','FcAddressId')
vsanIndex,=mibBuilder.importSymbols(_K,_L)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_e,'InterfaceIndex',_f)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_k,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention',_I)
ciscoFiconMIB=ModuleIdentity((1,3,6,1,4,1,9,9,375))
if mibBuilder.loadTexts:ciscoFiconMIB.setRevisions(('2006-04-07 00:00','2006-03-14 00:00','2005-10-21 00:00','2005-10-06 00:00','2005-06-01 00:00'))
class CficonPortNumOrAddr(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoFiconMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoFiconMIBNotifications=_CiscoFiconMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,375,0))
_CiscoFiconMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFiconMIBObjects=_CiscoFiconMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,375,1))
_CiscoFiconConfig_ObjectIdentity=ObjectIdentity
ciscoFiconConfig=_CiscoFiconConfig_ObjectIdentity((1,3,6,1,4,1,9,9,375,1,1))
_CficonPortSwapTable_Object=MibTable
cficonPortSwapTable=_CficonPortSwapTable_Object((1,3,6,1,4,1,9,9,375,1,1,1))
if mibBuilder.loadTexts:cficonPortSwapTable.setStatus(_B)
_CficonPortSwapEntry_Object=MibTableRow
cficonPortSwapEntry=_CficonPortSwapEntry_Object((1,3,6,1,4,1,9,9,375,1,1,1,1))
cficonPortSwapEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:cficonPortSwapEntry.setStatus(_B)
class _CficonPortSwapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CficonPortSwapIndex_Type.__name__=_D
_CficonPortSwapIndex_Object=MibTableColumn
cficonPortSwapIndex=_CficonPortSwapIndex_Object((1,3,6,1,4,1,9,9,375,1,1,1,1,1),_CficonPortSwapIndex_Type())
cficonPortSwapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonPortSwapIndex.setStatus(_B)
_CficonSwapPortNumberFirst_Type=CficonPortNumOrAddr
_CficonSwapPortNumberFirst_Object=MibTableColumn
cficonSwapPortNumberFirst=_CficonSwapPortNumberFirst_Object((1,3,6,1,4,1,9,9,375,1,1,1,1,2),_CficonSwapPortNumberFirst_Type())
cficonSwapPortNumberFirst.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSwapPortNumberFirst.setStatus(_B)
_CficonSwapPortNumberSecond_Type=CficonPortNumOrAddr
_CficonSwapPortNumberSecond_Object=MibTableColumn
cficonSwapPortNumberSecond=_CficonSwapPortNumberSecond_Object((1,3,6,1,4,1,9,9,375,1,1,1,1,3),_CficonSwapPortNumberSecond_Type())
cficonSwapPortNumberSecond.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSwapPortNumberSecond.setStatus(_B)
_CficonSwapPortEntryStatus_Type=RowStatus
_CficonSwapPortEntryStatus_Object=MibTableColumn
cficonSwapPortEntryStatus=_CficonSwapPortEntryStatus_Object((1,3,6,1,4,1,9,9,375,1,1,1,1,4),_CficonSwapPortEntryStatus_Type())
cficonSwapPortEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSwapPortEntryStatus.setStatus(_B)
_CficonVsanTable_Object=MibTable
cficonVsanTable=_CficonVsanTable_Object((1,3,6,1,4,1,9,9,375,1,1,2))
if mibBuilder.loadTexts:cficonVsanTable.setStatus(_B)
_CficonVsanEntry_Object=MibTableRow
cficonVsanEntry=_CficonVsanEntry_Object((1,3,6,1,4,1,9,9,375,1,1,2,1))
cficonVsanEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:cficonVsanEntry.setStatus(_B)
class _CficonVsanHostControl_Type(TruthValue):defaultValue=1
_CficonVsanHostControl_Type.__name__=_I
_CficonVsanHostControl_Object=MibTableColumn
cficonVsanHostControl=_CficonVsanHostControl_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,1),_CficonVsanHostControl_Type())
cficonVsanHostControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanHostControl.setStatus(_B)
class _CficonVsanHostControlSwOffline_Type(TruthValue):defaultValue=1
_CficonVsanHostControlSwOffline_Type.__name__=_I
_CficonVsanHostControlSwOffline_Object=MibTableColumn
cficonVsanHostControlSwOffline=_CficonVsanHostControlSwOffline_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,2),_CficonVsanHostControlSwOffline_Type())
cficonVsanHostControlSwOffline.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanHostControlSwOffline.setStatus(_B)
class _CficonVsanHostControlClkAlrtMode_Type(TruthValue):defaultValue=2
_CficonVsanHostControlClkAlrtMode_Type.__name__=_I
_CficonVsanHostControlClkAlrtMode_Object=MibTableColumn
cficonVsanHostControlClkAlrtMode=_CficonVsanHostControlClkAlrtMode_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,3),_CficonVsanHostControlClkAlrtMode_Type())
cficonVsanHostControlClkAlrtMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanHostControlClkAlrtMode.setStatus(_B)
class _CficonVsanSnmpControl_Type(TruthValue):defaultValue=1
_CficonVsanSnmpControl_Type.__name__=_I
_CficonVsanSnmpControl_Object=MibTableColumn
cficonVsanSnmpControl=_CficonVsanSnmpControl_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,4),_CficonVsanSnmpControl_Type())
cficonVsanSnmpControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanSnmpControl.setStatus(_B)
class _CficonVsanAutoSavePortAddrCfg_Type(TruthValue):defaultValue=2
_CficonVsanAutoSavePortAddrCfg_Type.__name__=_I
_CficonVsanAutoSavePortAddrCfg_Object=MibTableColumn
cficonVsanAutoSavePortAddrCfg=_CficonVsanAutoSavePortAddrCfg_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,5),_CficonVsanAutoSavePortAddrCfg_Type())
cficonVsanAutoSavePortAddrCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanAutoSavePortAddrCfg.setStatus(_B)
class _CficonVsanEnableCup_Type(TruthValue):defaultValue=1
_CficonVsanEnableCup_Type.__name__=_I
_CficonVsanEnableCup_Object=MibTableColumn
cficonVsanEnableCup=_CficonVsanEnableCup_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,6),_CficonVsanEnableCup_Type())
cficonVsanEnableCup.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanEnableCup.setStatus(_B)
class _CficonVsanCodePage_Type(Integer32):defaultValue=37;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(37,273,275,280,281,284,285,297,500)));namedValues=NamedValues(*(('usa',37),('germany',273),('brazil',275),('italy',280),('japan',281),('spain',284),('uk',285),('france',297),('interNational',500)))
_CficonVsanCodePage_Type.__name__=_D
_CficonVsanCodePage_Object=MibTableColumn
cficonVsanCodePage=_CficonVsanCodePage_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,7),_CficonVsanCodePage_Type())
cficonVsanCodePage.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanCodePage.setStatus(_B)
class _CficonVsanCharSet_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('charSet697',1))
_CficonVsanCharSet_Type.__name__=_D
_CficonVsanCharSet_Object=MibTableColumn
cficonVsanCharSet=_CficonVsanCharSet_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,8),_CficonVsanCharSet_Type())
cficonVsanCharSet.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanCharSet.setStatus(_B)
class _CficonVsanKeyCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CficonVsanKeyCounter_Type.__name__=_D
_CficonVsanKeyCounter_Object=MibTableColumn
cficonVsanKeyCounter=_CficonVsanKeyCounter_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,9),_CficonVsanKeyCounter_Type())
cficonVsanKeyCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonVsanKeyCounter.setStatus(_B)
class _CficonVsanUserAlertMode_Type(TruthValue):defaultValue=2
_CficonVsanUserAlertMode_Type.__name__=_I
_CficonVsanUserAlertMode_Object=MibTableColumn
cficonVsanUserAlertMode=_CficonVsanUserAlertMode_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,10),_CficonVsanUserAlertMode_Type())
cficonVsanUserAlertMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanUserAlertMode.setStatus(_B)
class _CficonVsanDeviceAllegience_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lockedByCLI',1),('lockedBySnmp',2),('lockedByHost',3),(_p,4)))
_CficonVsanDeviceAllegience_Type.__name__=_D
_CficonVsanDeviceAllegience_Object=MibTableColumn
cficonVsanDeviceAllegience=_CficonVsanDeviceAllegience_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,11),_CficonVsanDeviceAllegience_Type())
cficonVsanDeviceAllegience.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonVsanDeviceAllegience.setStatus(_B)
_CficonVsanTime_Type=DisplayString
_CficonVsanTime_Object=MibTableColumn
cficonVsanTime=_CficonVsanTime_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,12),_CficonVsanTime_Type())
cficonVsanTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonVsanTime.setStatus(_B)
class _CficonVsanHostOrDefaultTime_Type(TruthValue):defaultValue=2
_CficonVsanHostOrDefaultTime_Type.__name__=_I
_CficonVsanHostOrDefaultTime_Object=MibTableColumn
cficonVsanHostOrDefaultTime=_CficonVsanHostOrDefaultTime_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,13),_CficonVsanHostOrDefaultTime_Type())
cficonVsanHostOrDefaultTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonVsanHostOrDefaultTime.setStatus(_B)
_CficonVsanCupName_Type=SnmpAdminString
_CficonVsanCupName_Object=MibTableColumn
cficonVsanCupName=_CficonVsanCupName_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,14),_CficonVsanCupName_Type())
cficonVsanCupName.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanCupName.setStatus(_B)
class _CficonSetHostTimeControl_Type(TruthValue):defaultValue=1
_CficonSetHostTimeControl_Type.__name__=_I
_CficonSetHostTimeControl_Object=MibTableColumn
cficonSetHostTimeControl=_CficonSetHostTimeControl_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,15),_CficonSetHostTimeControl_Type())
cficonSetHostTimeControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSetHostTimeControl.setStatus(_B)
class _CficonVsanClearAllegience_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_CficonVsanClearAllegience_Type.__name__=_D
_CficonVsanClearAllegience_Object=MibTableColumn
cficonVsanClearAllegience=_CficonVsanClearAllegience_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,16),_CficonVsanClearAllegience_Type())
cficonVsanClearAllegience.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanClearAllegience.setStatus(_B)
_CficonVsanEntryStatus_Type=RowStatus
_CficonVsanEntryStatus_Object=MibTableColumn
cficonVsanEntryStatus=_CficonVsanEntryStatus_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,17),_CficonVsanEntryStatus_Type())
cficonVsanEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanEntryStatus.setStatus(_B)
class _CficonVsanFiconState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('offline',1),('online',2)))
_CficonVsanFiconState_Type.__name__=_D
_CficonVsanFiconState_Object=MibTableColumn
cficonVsanFiconState=_CficonVsanFiconState_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,18),_CficonVsanFiconState_Type())
cficonVsanFiconState.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonVsanFiconState.setStatus(_B)
_CficonVsanSerialNum_Type=SnmpAdminString
_CficonVsanSerialNum_Object=MibTableColumn
cficonVsanSerialNum=_CficonVsanSerialNum_Object((1,3,6,1,4,1,9,9,375,1,1,2,1,19),_CficonVsanSerialNum_Type())
cficonVsanSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonVsanSerialNum.setStatus(_B)
_CficonPortTable_Object=MibTable
cficonPortTable=_CficonPortTable_Object((1,3,6,1,4,1,9,9,375,1,1,3))
if mibBuilder.loadTexts:cficonPortTable.setStatus(_B)
_CficonPortEntry_Object=MibTableRow
cficonPortEntry=_CficonPortEntry_Object((1,3,6,1,4,1,9,9,375,1,1,3,1))
cficonPortEntry.setIndexNames((0,_K,_L),(0,_A,_g),(0,_A,_q))
if mibBuilder.loadTexts:cficonPortEntry.setStatus(_B)
_CficonPortAddr_Type=CficonPortNumOrAddr
_CficonPortAddr_Object=MibTableColumn
cficonPortAddr=_CficonPortAddr_Object((1,3,6,1,4,1,9,9,375,1,1,3,1,1),_CficonPortAddr_Type())
cficonPortAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonPortAddr.setStatus(_B)
_CficonPortBlock_Type=TruthValue
_CficonPortBlock_Object=MibTableColumn
cficonPortBlock=_CficonPortBlock_Object((1,3,6,1,4,1,9,9,375,1,1,3,1,2),_CficonPortBlock_Type())
cficonPortBlock.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonPortBlock.setStatus(_B)
_CficonPortName_Type=SnmpAdminString
_CficonPortName_Object=MibTableColumn
cficonPortName=_CficonPortName_Object((1,3,6,1,4,1,9,9,375,1,1,3,1,3),_CficonPortName_Type())
cficonPortName.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonPortName.setStatus(_B)
class _CficonProhibitPortNumbers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CficonProhibitPortNumbers_Type.__name__=_H
_CficonProhibitPortNumbers_Object=MibTableColumn
cficonProhibitPortNumbers=_CficonProhibitPortNumbers_Object((1,3,6,1,4,1,9,9,375,1,1,3,1,4),_CficonProhibitPortNumbers_Type())
cficonProhibitPortNumbers.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonProhibitPortNumbers.setStatus(_B)
_CficonPortRunCfgTable_Object=MibTable
cficonPortRunCfgTable=_CficonPortRunCfgTable_Object((1,3,6,1,4,1,9,9,375,1,1,4))
if mibBuilder.loadTexts:cficonPortRunCfgTable.setStatus(_B)
_CficonPortRunCfgEntry_Object=MibTableRow
cficonPortRunCfgEntry=_CficonPortRunCfgEntry_Object((1,3,6,1,4,1,9,9,375,1,1,4,1))
cficonPortRunCfgEntry.setIndexNames((0,_K,_L),(0,_A,_r))
if mibBuilder.loadTexts:cficonPortRunCfgEntry.setStatus(_B)
_CficonPortRunCfgAddr_Type=CficonPortNumOrAddr
_CficonPortRunCfgAddr_Object=MibTableColumn
cficonPortRunCfgAddr=_CficonPortRunCfgAddr_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,1),_CficonPortRunCfgAddr_Type())
cficonPortRunCfgAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonPortRunCfgAddr.setStatus(_B)
_CficonPortRunCfgBlock_Type=TruthValue
_CficonPortRunCfgBlock_Object=MibTableColumn
cficonPortRunCfgBlock=_CficonPortRunCfgBlock_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,2),_CficonPortRunCfgBlock_Type())
cficonPortRunCfgBlock.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonPortRunCfgBlock.setStatus(_B)
_CficonPortRunCfgName_Type=SnmpAdminString
_CficonPortRunCfgName_Object=MibTableColumn
cficonPortRunCfgName=_CficonPortRunCfgName_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,3),_CficonPortRunCfgName_Type())
cficonPortRunCfgName.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonPortRunCfgName.setStatus(_B)
class _CficonRunCfgProhibitPrtNums_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_CficonRunCfgProhibitPrtNums_Type.__name__=_H
_CficonRunCfgProhibitPrtNums_Object=MibTableColumn
cficonRunCfgProhibitPrtNums=_CficonRunCfgProhibitPrtNums_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,4),_CficonRunCfgProhibitPrtNums_Type())
cficonRunCfgProhibitPrtNums.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonRunCfgProhibitPrtNums.setStatus(_B)
class _CficonRunCfgTypeNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CficonRunCfgTypeNumber_Type.__name__=_M
_CficonRunCfgTypeNumber_Object=MibTableColumn
cficonRunCfgTypeNumber=_CficonRunCfgTypeNumber_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,5),_CficonRunCfgTypeNumber_Type())
cficonRunCfgTypeNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgTypeNumber.setStatus(_B)
class _CficonRunCfgModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CficonRunCfgModelNumber_Type.__name__=_M
_CficonRunCfgModelNumber_Object=MibTableColumn
cficonRunCfgModelNumber=_CficonRunCfgModelNumber_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,6),_CficonRunCfgModelNumber_Type())
cficonRunCfgModelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgModelNumber.setStatus(_B)
class _CficonRunCfgManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CficonRunCfgManufacturer_Type.__name__=_M
_CficonRunCfgManufacturer_Object=MibTableColumn
cficonRunCfgManufacturer=_CficonRunCfgManufacturer_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,7),_CficonRunCfgManufacturer_Type())
cficonRunCfgManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgManufacturer.setStatus(_B)
class _CficonRunCfgPlantOfMfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CficonRunCfgPlantOfMfg_Type.__name__=_M
_CficonRunCfgPlantOfMfg_Object=MibTableColumn
cficonRunCfgPlantOfMfg=_CficonRunCfgPlantOfMfg_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,8),_CficonRunCfgPlantOfMfg_Type())
cficonRunCfgPlantOfMfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgPlantOfMfg.setStatus(_B)
class _CficonRunCfgSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CficonRunCfgSerialNumber_Type.__name__=_M
_CficonRunCfgSerialNumber_Object=MibTableColumn
cficonRunCfgSerialNumber=_CficonRunCfgSerialNumber_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,9),_CficonRunCfgSerialNumber_Type())
cficonRunCfgSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgSerialNumber.setStatus(_B)
class _CficonRunCfgUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('channel',1),('controlUnit',2),('fabric',3),('unknown',4)))
_CficonRunCfgUnitType_Type.__name__=_D
_CficonRunCfgUnitType_Object=MibTableColumn
cficonRunCfgUnitType=_CficonRunCfgUnitType_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,10),_CficonRunCfgUnitType_Type())
cficonRunCfgUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgUnitType.setStatus(_B)
class _CficonRunCfgPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CficonRunCfgPortId_Type.__name__=_D
_CficonRunCfgPortId_Object=MibTableColumn
cficonRunCfgPortId=_CficonRunCfgPortId_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,11),_CficonRunCfgPortId_Type())
cficonRunCfgPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRunCfgPortId.setStatus(_B)
class _CficonRunCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),('invalid',2),('old',3)))
_CficonRunCfgStatus_Type.__name__=_D
_CficonRunCfgStatus_Object=MibTableColumn
cficonRunCfgStatus=_CficonRunCfgStatus_Object((1,3,6,1,4,1,9,9,375,1,1,4,1,12),_CficonRunCfgStatus_Type())
cficonRunCfgStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonRunCfgStatus.setStatus(_B)
_CficonCfgFileTable_Object=MibTable
cficonCfgFileTable=_CficonCfgFileTable_Object((1,3,6,1,4,1,9,9,375,1,1,5))
if mibBuilder.loadTexts:cficonCfgFileTable.setStatus(_B)
_CficonCfgFileEntry_Object=MibTableRow
cficonCfgFileEntry=_CficonCfgFileEntry_Object((1,3,6,1,4,1,9,9,375,1,1,5,1))
cficonCfgFileEntry.setIndexNames((0,_K,_L),(0,_A,_g))
if mibBuilder.loadTexts:cficonCfgFileEntry.setStatus(_B)
class _CficonCfgFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CficonCfgFilename_Type.__name__=_N
_CficonCfgFilename_Object=MibTableColumn
cficonCfgFilename=_CficonCfgFilename_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,1),_CficonCfgFilename_Type())
cficonCfgFilename.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonCfgFilename.setStatus(_B)
class _CficonCfgFileDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CficonCfgFileDescr_Type.__name__=_N
_CficonCfgFileDescr_Object=MibTableColumn
cficonCfgFileDescr=_CficonCfgFileDescr_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,2),_CficonCfgFileDescr_Type())
cficonCfgFileDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonCfgFileDescr.setStatus(_B)
class _CficonCfgFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('locked',1),(_p,2)))
_CficonCfgFileStatus_Type.__name__=_D
_CficonCfgFileStatus_Object=MibTableColumn
cficonCfgFileStatus=_CficonCfgFileStatus_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,3),_CficonCfgFileStatus_Type())
cficonCfgFileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonCfgFileStatus.setStatus(_B)
_CficonCfgFileLastUpdated_Type=SnmpAdminString
_CficonCfgFileLastUpdated_Object=MibTableColumn
cficonCfgFileLastUpdated=_CficonCfgFileLastUpdated_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,4),_CficonCfgFileLastUpdated_Type())
cficonCfgFileLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonCfgFileLastUpdated.setStatus(_B)
class _CficonCfgFileCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('apply',1),('noOp',2),('open',3),('close',4)))
_CficonCfgFileCmd_Type.__name__=_D
_CficonCfgFileCmd_Object=MibTableColumn
cficonCfgFileCmd=_CficonCfgFileCmd_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,5),_CficonCfgFileCmd_Type())
cficonCfgFileCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonCfgFileCmd.setStatus(_B)
_CficonCfgFileRowStatus_Type=RowStatus
_CficonCfgFileRowStatus_Object=MibTableColumn
cficonCfgFileRowStatus=_CficonCfgFileRowStatus_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,6),_CficonCfgFileRowStatus_Type())
cficonCfgFileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonCfgFileRowStatus.setStatus(_B)
class _CficonCfgFileCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),(_s,2),(_t,3),('notApplicable',4)))
_CficonCfgFileCmdStatus_Type.__name__=_D
_CficonCfgFileCmdStatus_Object=MibTableColumn
cficonCfgFileCmdStatus=_CficonCfgFileCmdStatus_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,7),_CficonCfgFileCmdStatus_Type())
cficonCfgFileCmdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonCfgFileCmdStatus.setStatus(_B)
class _CficonCfgFileCmdErrorString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CficonCfgFileCmdErrorString_Type.__name__=_N
_CficonCfgFileCmdErrorString_Object=MibTableColumn
cficonCfgFileCmdErrorString=_CficonCfgFileCmdErrorString_Object((1,3,6,1,4,1,9,9,375,1,1,5,1,8),_CficonCfgFileCmdErrorString_Type())
cficonCfgFileCmdErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonCfgFileCmdErrorString.setStatus(_B)
_CficonPortNumIfTable_Object=MibTable
cficonPortNumIfTable=_CficonPortNumIfTable_Object((1,3,6,1,4,1,9,9,375,1,1,6))
if mibBuilder.loadTexts:cficonPortNumIfTable.setStatus(_B)
_CficonPortNumIfEntry_Object=MibTableRow
cficonPortNumIfEntry=_CficonPortNumIfEntry_Object((1,3,6,1,4,1,9,9,375,1,1,6,1))
cficonPortNumIfEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:cficonPortNumIfEntry.setStatus(_B)
_CficonPortNumber_Type=CficonPortNumOrAddr
_CficonPortNumber_Object=MibTableColumn
cficonPortNumber=_CficonPortNumber_Object((1,3,6,1,4,1,9,9,375,1,1,6,1,1),_CficonPortNumber_Type())
cficonPortNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonPortNumber.setStatus(_B)
_CficonPortIfIndex_Type=InterfaceIndex
_CficonPortIfIndex_Object=MibTableColumn
cficonPortIfIndex=_CficonPortIfIndex_Object((1,3,6,1,4,1,9,9,375,1,1,6,1,2),_CficonPortIfIndex_Type())
cficonPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonPortIfIndex.setStatus(_B)
_CficonPortAddrNumTable_Object=MibTable
cficonPortAddrNumTable=_CficonPortAddrNumTable_Object((1,3,6,1,4,1,9,9,375,1,1,7))
if mibBuilder.loadTexts:cficonPortAddrNumTable.setStatus(_B)
_CficonPortAddrNumEntry_Object=MibTableRow
cficonPortAddrNumEntry=_CficonPortAddrNumEntry_Object((1,3,6,1,4,1,9,9,375,1,1,7,1))
cficonPortAddrNumEntry.setIndexNames((0,_A,_v))
if mibBuilder.loadTexts:cficonPortAddrNumEntry.setStatus(_B)
_CficonPortAddrPortAddr_Type=CficonPortNumOrAddr
_CficonPortAddrPortAddr_Object=MibTableColumn
cficonPortAddrPortAddr=_CficonPortAddrPortAddr_Object((1,3,6,1,4,1,9,9,375,1,1,7,1,1),_CficonPortAddrPortAddr_Type())
cficonPortAddrPortAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonPortAddrPortAddr.setStatus(_B)
_CficonPortAddrPortNumber_Type=CficonPortNumOrAddr
_CficonPortAddrPortNumber_Object=MibTableColumn
cficonPortAddrPortNumber=_CficonPortAddrPortNumber_Object((1,3,6,1,4,1,9,9,375,1,1,7,1,2),_CficonPortAddrPortNumber_Type())
cficonPortAddrPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortAddrPortNumber.setStatus(_B)
_CficonPortNumAddrTable_Object=MibTable
cficonPortNumAddrTable=_CficonPortNumAddrTable_Object((1,3,6,1,4,1,9,9,375,1,1,8))
if mibBuilder.loadTexts:cficonPortNumAddrTable.setStatus(_B)
_CficonPortNumAddrEntry_Object=MibTableRow
cficonPortNumAddrEntry=_CficonPortNumAddrEntry_Object((1,3,6,1,4,1,9,9,375,1,1,8,1))
cficonPortNumAddrEntry.setIndexNames((0,_A,_w))
if mibBuilder.loadTexts:cficonPortNumAddrEntry.setStatus(_B)
_PortAddrPortNumber_Type=CficonPortNumOrAddr
_PortAddrPortNumber_Object=MibTableColumn
portAddrPortNumber=_PortAddrPortNumber_Object((1,3,6,1,4,1,9,9,375,1,1,8,1,1),_PortAddrPortNumber_Type())
portAddrPortNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:portAddrPortNumber.setStatus(_B)
_PortAddress_Type=CficonPortNumOrAddr
_PortAddress_Object=MibTableColumn
portAddress=_PortAddress_Object((1,3,6,1,4,1,9,9,375,1,1,8,1,2),_PortAddress_Type())
portAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:portAddress.setStatus(_B)
_CficonDirHistTable_Object=MibTable
cficonDirHistTable=_CficonDirHistTable_Object((1,3,6,1,4,1,9,9,375,1,1,9))
if mibBuilder.loadTexts:cficonDirHistTable.setStatus(_B)
_CficonDirHistEntry_Object=MibTableRow
cficonDirHistEntry=_CficonDirHistEntry_Object((1,3,6,1,4,1,9,9,375,1,1,9,1))
cficonDirHistEntry.setIndexNames((0,_K,_L),(0,_A,_x))
if mibBuilder.loadTexts:cficonDirHistEntry.setStatus(_B)
class _CficonDirHistKeyCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CficonDirHistKeyCounter_Type.__name__=_D
_CficonDirHistKeyCounter_Object=MibTableColumn
cficonDirHistKeyCounter=_CficonDirHistKeyCounter_Object((1,3,6,1,4,1,9,9,375,1,1,9,1,1),_CficonDirHistKeyCounter_Type())
cficonDirHistKeyCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonDirHistKeyCounter.setStatus(_B)
class _CficonDirHistPortNumbers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CficonDirHistPortNumbers_Type.__name__=_H
_CficonDirHistPortNumbers_Object=MibTableColumn
cficonDirHistPortNumbers=_CficonDirHistPortNumbers_Object((1,3,6,1,4,1,9,9,375,1,1,9,1,2),_CficonDirHistPortNumbers_Type())
cficonDirHistPortNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonDirHistPortNumbers.setStatus(_B)
_CficonStatsTable_Object=MibTable
cficonStatsTable=_CficonStatsTable_Object((1,3,6,1,4,1,9,9,375,1,1,10))
if mibBuilder.loadTexts:cficonStatsTable.setStatus(_B)
_CficonStatsEntry_Object=MibTableRow
cficonStatsEntry=_CficonStatsEntry_Object((1,3,6,1,4,1,9,9,375,1,1,10,1))
cficonStatsEntry.setIndexNames((0,_e,_f))
if mibBuilder.loadTexts:cficonStatsEntry.setStatus(_B)
_CfStatsFramePacingTime_Type=Counter32
_CfStatsFramePacingTime_Object=MibTableColumn
cfStatsFramePacingTime=_CfStatsFramePacingTime_Object((1,3,6,1,4,1,9,9,375,1,1,10,1,1),_CfStatsFramePacingTime_Type())
cfStatsFramePacingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfStatsFramePacingTime.setStatus(_B)
_CfStatsDispErrorsInFrame_Type=Counter32
_CfStatsDispErrorsInFrame_Object=MibTableColumn
cfStatsDispErrorsInFrame=_CfStatsDispErrorsInFrame_Object((1,3,6,1,4,1,9,9,375,1,1,10,1,2),_CfStatsDispErrorsInFrame_Type())
cfStatsDispErrorsInFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:cfStatsDispErrorsInFrame.setStatus(_B)
_CfStatsEOFErrs_Type=Counter32
_CfStatsEOFErrs_Object=MibTableColumn
cfStatsEOFErrs=_CfStatsEOFErrs_Object((1,3,6,1,4,1,9,9,375,1,1,10,1,3),_CfStatsEOFErrs_Type())
cfStatsEOFErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfStatsEOFErrs.setStatus(_B)
_CfStatsDispErrsOutOfFrame_Type=Counter32
_CfStatsDispErrsOutOfFrame_Object=MibTableColumn
cfStatsDispErrsOutOfFrame=_CfStatsDispErrsOutOfFrame_Object((1,3,6,1,4,1,9,9,375,1,1,10,1,4),_CfStatsDispErrsOutOfFrame_Type())
cfStatsDispErrsOutOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:cfStatsDispErrsOutOfFrame.setStatus(_B)
_CfStatsInvalidOrderSets_Type=Counter32
_CfStatsInvalidOrderSets_Object=MibTableColumn
cfStatsInvalidOrderSets=_CfStatsInvalidOrderSets_Object((1,3,6,1,4,1,9,9,375,1,1,10,1,5),_CfStatsInvalidOrderSets_Type())
cfStatsInvalidOrderSets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfStatsInvalidOrderSets.setStatus(_B)
_CfStatsErrorSummary_Type=Counter32
_CfStatsErrorSummary_Object=MibTableColumn
cfStatsErrorSummary=_CfStatsErrorSummary_Object((1,3,6,1,4,1,9,9,375,1,1,10,1,6),_CfStatsErrorSummary_Type())
cfStatsErrorSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:cfStatsErrorSummary.setStatus(_B)
class _CficonShowPorts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),('installed',2)))
_CficonShowPorts_Type.__name__=_D
_CficonShowPorts_Object=MibScalar
cficonShowPorts=_CficonShowPorts_Object((1,3,6,1,4,1,9,9,375,1,1,11),_CficonShowPorts_Type())
cficonShowPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonShowPorts.setStatus(_B)
_CficonLinkIncidentTable_Object=MibTable
cficonLinkIncidentTable=_CficonLinkIncidentTable_Object((1,3,6,1,4,1,9,9,375,1,1,12))
if mibBuilder.loadTexts:cficonLinkIncidentTable.setStatus(_B)
_CficonLinkIncidentEntry_Object=MibTableRow
cficonLinkIncidentEntry=_CficonLinkIncidentEntry_Object((1,3,6,1,4,1,9,9,375,1,1,12,1))
cficonLinkIncidentEntry.setIndexNames((0,_e,_f))
if mibBuilder.loadTexts:cficonLinkIncidentEntry.setStatus(_B)
class _CficonLinkIncident_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('bitErrThreshExceeded',2),('lossOfSignalOrSync',3),('nosReceived',4),('primitiveSeqTimeOut',5),('invalidPrimitiveSeq',6)))
_CficonLinkIncident_Type.__name__=_D
_CficonLinkIncident_Object=MibTableColumn
cficonLinkIncident=_CficonLinkIncident_Object((1,3,6,1,4,1,9,9,375,1,1,12,1,1),_CficonLinkIncident_Type())
cficonLinkIncident.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonLinkIncident.setStatus(_B)
class _CficonLinkIncidentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CficonLinkIncidentTime_Type.__name__=_M
_CficonLinkIncidentTime_Object=MibTableColumn
cficonLinkIncidentTime=_CficonLinkIncidentTime_Object((1,3,6,1,4,1,9,9,375,1,1,12,1,2),_CficonLinkIncidentTime_Type())
cficonLinkIncidentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonLinkIncidentTime.setStatus(_B)
class _CficonLinkIncidentClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_CficonLinkIncidentClear_Type.__name__=_D
_CficonLinkIncidentClear_Object=MibTableColumn
cficonLinkIncidentClear=_CficonLinkIncidentClear_Object((1,3,6,1,4,1,9,9,375,1,1,12,1,3),_CficonLinkIncidentClear_Type())
cficonLinkIncidentClear.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonLinkIncidentClear.setStatus(_B)
_CficonCfgFileCupNameTable_Object=MibTable
cficonCfgFileCupNameTable=_CficonCfgFileCupNameTable_Object((1,3,6,1,4,1,9,9,375,1,1,13))
if mibBuilder.loadTexts:cficonCfgFileCupNameTable.setStatus(_B)
_CficonCfgFileCupNameEntry_Object=MibTableRow
cficonCfgFileCupNameEntry=_CficonCfgFileCupNameEntry_Object((1,3,6,1,4,1,9,9,375,1,1,13,1))
cficonCfgFileCupNameEntry.setIndexNames((0,_K,_L),(0,_A,_g))
if mibBuilder.loadTexts:cficonCfgFileCupNameEntry.setStatus(_B)
class _CficonCfgFileCupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_CficonCfgFileCupName_Type.__name__=_N
_CficonCfgFileCupName_Object=MibTableColumn
cficonCfgFileCupName=_CficonCfgFileCupName_Object((1,3,6,1,4,1,9,9,375,1,1,13,1,1),_CficonCfgFileCupName_Type())
cficonCfgFileCupName.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonCfgFileCupName.setStatus(_B)
_CficonConfigCopyTable_Object=MibTable
cficonConfigCopyTable=_CficonConfigCopyTable_Object((1,3,6,1,4,1,9,9,375,1,1,14))
if mibBuilder.loadTexts:cficonConfigCopyTable.setStatus(_B)
_CficonConfigCopyEntry_Object=MibTableRow
cficonConfigCopyEntry=_CficonConfigCopyEntry_Object((1,3,6,1,4,1,9,9,375,1,1,14,1))
cficonConfigCopyEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:cficonConfigCopyEntry.setStatus(_B)
class _CficonConfigCopyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CficonConfigCopyIndex_Type.__name__=_k
_CficonConfigCopyIndex_Object=MibTableColumn
cficonConfigCopyIndex=_CficonConfigCopyIndex_Object((1,3,6,1,4,1,9,9,375,1,1,14,1,1),_CficonConfigCopyIndex_Type())
cficonConfigCopyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonConfigCopyIndex.setStatus(_B)
class _CficonCopyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_s,1),(_l,2),(_t,3)))
_CficonCopyState_Type.__name__=_D
_CficonCopyState_Object=MibTableColumn
cficonCopyState=_CficonCopyState_Object((1,3,6,1,4,1,9,9,375,1,1,14,1,2),_CficonCopyState_Type())
cficonCopyState.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonCopyState.setStatus(_B)
_CficonCopyFailReason_Type=SnmpAdminString
_CficonCopyFailReason_Object=MibTableColumn
cficonCopyFailReason=_CficonCopyFailReason_Object((1,3,6,1,4,1,9,9,375,1,1,14,1,3),_CficonCopyFailReason_Type())
cficonCopyFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonCopyFailReason.setStatus(_B)
_CficonCopyEntryRowStatus_Type=RowStatus
_CficonCopyEntryRowStatus_Object=MibTableColumn
cficonCopyEntryRowStatus=_CficonCopyEntryRowStatus_Object((1,3,6,1,4,1,9,9,375,1,1,14,1,4),_CficonCopyEntryRowStatus_Type())
cficonCopyEntryRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonCopyEntryRowStatus.setStatus(_B)
class _CficonAutoSaveState_Type(TruthValue):defaultValue=2
_CficonAutoSaveState_Type.__name__=_I
_CficonAutoSaveState_Object=MibScalar
cficonAutoSaveState=_CficonAutoSaveState_Object((1,3,6,1,4,1,9,9,375,1,1,15),_CficonAutoSaveState_Type())
cficonAutoSaveState.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonAutoSaveState.setStatus(_B)
_CiscoFiconPortMap_ObjectIdentity=ObjectIdentity
ciscoFiconPortMap=_CiscoFiconPortMap_ObjectIdentity((1,3,6,1,4,1,9,9,375,1,1,16))
class _CficonPortMap1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMap1_Type.__name__=_H
_CficonPortMap1_Object=MibScalar
cficonPortMap1=_CficonPortMap1_Object((1,3,6,1,4,1,9,9,375,1,1,16,1),_CficonPortMap1_Type())
cficonPortMap1.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMap1.setStatus(_J)
class _CficonPortMap2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMap2_Type.__name__=_H
_CficonPortMap2_Object=MibScalar
cficonPortMap2=_CficonPortMap2_Object((1,3,6,1,4,1,9,9,375,1,1,16,2),_CficonPortMap2_Type())
cficonPortMap2.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMap2.setStatus(_J)
class _CficonPortMap3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMap3_Type.__name__=_H
_CficonPortMap3_Object=MibScalar
cficonPortMap3=_CficonPortMap3_Object((1,3,6,1,4,1,9,9,375,1,1,16,3),_CficonPortMap3_Type())
cficonPortMap3.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMap3.setStatus(_J)
class _CficonPortMap4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMap4_Type.__name__=_H
_CficonPortMap4_Object=MibScalar
cficonPortMap4=_CficonPortMap4_Object((1,3,6,1,4,1,9,9,375,1,1,16,4),_CficonPortMap4_Type())
cficonPortMap4.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMap4.setStatus(_J)
class _CficonPortMap5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMap5_Type.__name__=_H
_CficonPortMap5_Object=MibScalar
cficonPortMap5=_CficonPortMap5_Object((1,3,6,1,4,1,9,9,375,1,1,16,5),_CficonPortMap5_Type())
cficonPortMap5.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMap5.setStatus(_J)
class _CficonPortMap6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMap6_Type.__name__=_H
_CficonPortMap6_Object=MibScalar
cficonPortMap6=_CficonPortMap6_Object((1,3,6,1,4,1,9,9,375,1,1,16,6),_CficonPortMap6_Type())
cficonPortMap6.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMap6.setStatus(_J)
class _CficonPortMapMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CficonPortMapMax_Type.__name__=_D
_CficonPortMapMax_Object=MibScalar
cficonPortMapMax=_CficonPortMapMax_Object((1,3,6,1,4,1,9,9,375,1,1,16,7),_CficonPortMapMax_Type())
cficonPortMapMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMapMax.setStatus(_B)
_CficonPortMapTable_Object=MibTable
cficonPortMapTable=_CficonPortMapTable_Object((1,3,6,1,4,1,9,9,375,1,1,16,8))
if mibBuilder.loadTexts:cficonPortMapTable.setStatus(_B)
_CficonPortMapEntry_Object=MibTableRow
cficonPortMapEntry=_CficonPortMapEntry_Object((1,3,6,1,4,1,9,9,375,1,1,16,8,1))
cficonPortMapEntry.setIndexNames((0,_A,_z))
if mibBuilder.loadTexts:cficonPortMapEntry.setStatus(_B)
class _CficonPortMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CficonPortMapIndex_Type.__name__=_D
_CficonPortMapIndex_Object=MibTableColumn
cficonPortMapIndex=_CficonPortMapIndex_Object((1,3,6,1,4,1,9,9,375,1,1,16,8,1,1),_CficonPortMapIndex_Type())
cficonPortMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonPortMapIndex.setStatus(_B)
class _CficonPortMapObj_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CficonPortMapObj_Type.__name__=_H
_CficonPortMapObj_Object=MibTableColumn
cficonPortMapObj=_CficonPortMapObj_Object((1,3,6,1,4,1,9,9,375,1,1,16,8,1,2),_CficonPortMapObj_Type())
cficonPortMapObj.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonPortMapObj.setStatus(_B)
_CficonSlotPortNumTable_Object=MibTable
cficonSlotPortNumTable=_CficonSlotPortNumTable_Object((1,3,6,1,4,1,9,9,375,1,1,17))
if mibBuilder.loadTexts:cficonSlotPortNumTable.setStatus(_B)
_CficonSlotPortNumEntry_Object=MibTableRow
cficonSlotPortNumEntry=_CficonSlotPortNumEntry_Object((1,3,6,1,4,1,9,9,375,1,1,17,1))
cficonSlotPortNumEntry.setIndexNames((0,_A,_A0))
if mibBuilder.loadTexts:cficonSlotPortNumEntry.setStatus(_B)
class _CficonSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CficonSlotIndex_Type.__name__=_D
_CficonSlotIndex_Object=MibTableColumn
cficonSlotIndex=_CficonSlotIndex_Object((1,3,6,1,4,1,9,9,375,1,1,17,1,1),_CficonSlotIndex_Type())
cficonSlotIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonSlotIndex.setStatus(_B)
class _CficonSlotReservedPN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CficonSlotReservedPN_Type.__name__=_H
_CficonSlotReservedPN_Object=MibTableColumn
cficonSlotReservedPN=_CficonSlotReservedPN_Object((1,3,6,1,4,1,9,9,375,1,1,17,1,2),_CficonSlotReservedPN_Type())
cficonSlotReservedPN.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonSlotReservedPN.setStatus(_B)
class _CficonLogicReservedPN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CficonLogicReservedPN_Type.__name__=_H
_CficonLogicReservedPN_Object=MibScalar
cficonLogicReservedPN=_CficonLogicReservedPN_Object((1,3,6,1,4,1,9,9,375,1,1,18),_CficonLogicReservedPN_Type())
cficonLogicReservedPN.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonLogicReservedPN.setStatus(_B)
_CficonRlirErlTable_Object=MibTable
cficonRlirErlTable=_CficonRlirErlTable_Object((1,3,6,1,4,1,9,9,375,1,1,19))
if mibBuilder.loadTexts:cficonRlirErlTable.setStatus(_B)
_CficonRlirErlEntry_Object=MibTableRow
cficonRlirErlEntry=_CficonRlirErlEntry_Object((1,3,6,1,4,1,9,9,375,1,1,19,1))
cficonRlirErlEntry.setIndexNames((0,_K,_L),(0,_A,_A1),(0,_A,_A2))
if mibBuilder.loadTexts:cficonRlirErlEntry.setStatus(_B)
_CficonRlirErlFcId_Type=FcAddressId
_CficonRlirErlFcId_Object=MibTableColumn
cficonRlirErlFcId=_CficonRlirErlFcId_Object((1,3,6,1,4,1,9,9,375,1,1,19,1,1),_CficonRlirErlFcId_Type())
cficonRlirErlFcId.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonRlirErlFcId.setStatus(_B)
class _CficonRlirErlFormat_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CficonRlirErlFormat_Type.__name__=_k
_CficonRlirErlFormat_Object=MibTableColumn
cficonRlirErlFormat=_CficonRlirErlFormat_Object((1,3,6,1,4,1,9,9,375,1,1,19,1,2),_CficonRlirErlFormat_Type())
cficonRlirErlFormat.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonRlirErlFormat.setStatus(_B)
class _CficonRlirErlRegType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conditionalRx',1),('alwaysRx',2)))
_CficonRlirErlRegType_Type.__name__=_D
_CficonRlirErlRegType_Object=MibTableColumn
cficonRlirErlRegType=_CficonRlirErlRegType_Object((1,3,6,1,4,1,9,9,375,1,1,19,1,3),_CficonRlirErlRegType_Type())
cficonRlirErlRegType.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonRlirErlRegType.setStatus(_B)
_CficonInterfaceSwapTable_Object=MibTable
cficonInterfaceSwapTable=_CficonInterfaceSwapTable_Object((1,3,6,1,4,1,9,9,375,1,1,20))
if mibBuilder.loadTexts:cficonInterfaceSwapTable.setStatus(_B)
_CficonInterfaceSwapEntry_Object=MibTableRow
cficonInterfaceSwapEntry=_CficonInterfaceSwapEntry_Object((1,3,6,1,4,1,9,9,375,1,1,20,1))
cficonInterfaceSwapEntry.setIndexNames((0,_A,_A3))
if mibBuilder.loadTexts:cficonInterfaceSwapEntry.setStatus(_B)
class _CficonInterfaceSwapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CficonInterfaceSwapIndex_Type.__name__=_D
_CficonInterfaceSwapIndex_Object=MibTableColumn
cficonInterfaceSwapIndex=_CficonInterfaceSwapIndex_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,1),_CficonInterfaceSwapIndex_Type())
cficonInterfaceSwapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cficonInterfaceSwapIndex.setStatus(_B)
_CficonSwapInterfaceIndexFirst_Type=InterfaceIndex
_CficonSwapInterfaceIndexFirst_Object=MibTableColumn
cficonSwapInterfaceIndexFirst=_CficonSwapInterfaceIndexFirst_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,2),_CficonSwapInterfaceIndexFirst_Type())
cficonSwapInterfaceIndexFirst.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSwapInterfaceIndexFirst.setStatus(_B)
_CficonSwapInterfaceIndexSecond_Type=InterfaceIndex
_CficonSwapInterfaceIndexSecond_Object=MibTableColumn
cficonSwapInterfaceIndexSecond=_CficonSwapInterfaceIndexSecond_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,3),_CficonSwapInterfaceIndexSecond_Type())
cficonSwapInterfaceIndexSecond.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSwapInterfaceIndexSecond.setStatus(_B)
class _CficonSwapInterfaceActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pending',1),('executing',2),(_l,3),('failure',4)))
_CficonSwapInterfaceActionStatus_Type.__name__=_D
_CficonSwapInterfaceActionStatus_Object=MibTableColumn
cficonSwapInterfaceActionStatus=_CficonSwapInterfaceActionStatus_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,4),_CficonSwapInterfaceActionStatus_Type())
cficonSwapInterfaceActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonSwapInterfaceActionStatus.setStatus(_B)
class _CficonSwapInterfaceFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),('none',2),('dmFailure',3),('ficonFailure',4),('pmFailure',5),('psmFailure',6),('qosFailure',7),('spanFailure',8),('zsFailure',9)))
_CficonSwapInterfaceFailReason_Type.__name__=_D
_CficonSwapInterfaceFailReason_Object=MibTableColumn
cficonSwapInterfaceFailReason=_CficonSwapInterfaceFailReason_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,5),_CficonSwapInterfaceFailReason_Type())
cficonSwapInterfaceFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonSwapInterfaceFailReason.setStatus(_B)
_CficonSwapInterfaceSystemError_Type=SnmpAdminString
_CficonSwapInterfaceSystemError_Object=MibTableColumn
cficonSwapInterfaceSystemError=_CficonSwapInterfaceSystemError_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,6),_CficonSwapInterfaceSystemError_Type())
cficonSwapInterfaceSystemError.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonSwapInterfaceSystemError.setStatus(_B)
_CficonSwapInterfaceEntryStatus_Type=RowStatus
_CficonSwapInterfaceEntryStatus_Object=MibTableColumn
cficonSwapInterfaceEntryStatus=_CficonSwapInterfaceEntryStatus_Object((1,3,6,1,4,1,9,9,375,1,1,20,1,7),_CficonSwapInterfaceEntryStatus_Type())
cficonSwapInterfaceEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cficonSwapInterfaceEntryStatus.setStatus(_B)
class _CficonInterfaceSwapNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CficonInterfaceSwapNextIndex_Type.__name__=_D
_CficonInterfaceSwapNextIndex_Object=MibScalar
cficonInterfaceSwapNextIndex=_CficonInterfaceSwapNextIndex_Object((1,3,6,1,4,1,9,9,375,1,1,21),_CficonInterfaceSwapNextIndex_Type())
cficonInterfaceSwapNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cficonInterfaceSwapNextIndex.setStatus(_B)
_CiscoFiconGlobal_ObjectIdentity=ObjectIdentity
ciscoFiconGlobal=_CiscoFiconGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,375,1,2))
_CficonDefaultPortBlock_Type=TruthValue
_CficonDefaultPortBlock_Object=MibScalar
cficonDefaultPortBlock=_CficonDefaultPortBlock_Object((1,3,6,1,4,1,9,9,375,1,2,1),_CficonDefaultPortBlock_Type())
cficonDefaultPortBlock.setMaxAccess(_G)
if mibBuilder.loadTexts:cficonDefaultPortBlock.setStatus(_B)
_CiscoFiconMIBConform_ObjectIdentity=ObjectIdentity
ciscoFiconMIBConform=_CiscoFiconMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,375,2))
_CiscoFiconCompliances_ObjectIdentity=ObjectIdentity
ciscoFiconCompliances=_CiscoFiconCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,375,2,1))
_CiscoFiconGroups_ObjectIdentity=ObjectIdentity
ciscoFiconGroups=_CiscoFiconGroups_ObjectIdentity((1,3,6,1,4,1,9,9,375,2,2))
cficonPortSwapGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,1))
cficonPortSwapGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:cficonPortSwapGroup.setStatus(_B)
cficonVsanGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,2))
cficonVsanGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:cficonVsanGroup.setStatus(_B)
cficonPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,3))
cficonPortGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:cficonPortGroup.setStatus(_B)
cficonPortRunCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,4))
cficonPortRunCfgGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_m),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:cficonPortRunCfgGroup.setStatus(_B)
cficonCfgFileGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,5))
cficonCfgFileGroup.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:cficonCfgFileGroup.setStatus(_B)
cficonPortNumIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,6))
cficonPortNumIfGroup.setObjects((_A,_Ak))
if mibBuilder.loadTexts:cficonPortNumIfGroup.setStatus(_B)
cficonPortAddrNumGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,7))
cficonPortAddrNumGroup.setObjects((_A,_Al))
if mibBuilder.loadTexts:cficonPortAddrNumGroup.setStatus(_B)
cficonPortNumAddrGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,8))
cficonPortNumAddrGroup.setObjects((_A,_Am))
if mibBuilder.loadTexts:cficonPortNumAddrGroup.setStatus(_B)
cficonDirHistGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,9))
cficonDirHistGroup.setObjects((_A,_An))
if mibBuilder.loadTexts:cficonDirHistGroup.setStatus(_B)
cficonStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,10))
cficonStatsGroup.setObjects(*((_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:cficonStatsGroup.setStatus(_B)
cifconShowPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,11))
cifconShowPortGroup.setObjects((_A,_Au))
if mibBuilder.loadTexts:cifconShowPortGroup.setStatus(_B)
cficonLinkIncidentGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,12))
cficonLinkIncidentGroup.setObjects(*((_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:cficonLinkIncidentGroup.setStatus(_B)
cficonCfgFileCupNameGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,13))
cficonCfgFileCupNameGroup.setObjects((_A,_Ay))
if mibBuilder.loadTexts:cficonCfgFileCupNameGroup.setStatus(_B)
cficonConfigCopyGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,14))
cficonConfigCopyGroup.setObjects(*((_A,_Az),(_A,_A_),(_A,_B0)))
if mibBuilder.loadTexts:cficonConfigCopyGroup.setStatus(_B)
cficonAutoSaveStateGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,15))
cficonAutoSaveStateGroup.setObjects((_A,_B1))
if mibBuilder.loadTexts:cficonAutoSaveStateGroup.setStatus(_B)
cficonPortMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,16))
cficonPortMapGroup.setObjects(*((_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:cficonPortMapGroup.setStatus(_J)
cficonPortMapGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,18))
cficonPortMapGroupRev1.setObjects(*((_A,_B8),(_A,_B9)))
if mibBuilder.loadTexts:cficonPortMapGroupRev1.setStatus(_B)
cficonReservedPortNumGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,19))
cficonReservedPortNumGroup.setObjects(*((_A,_BA),(_A,_BB)))
if mibBuilder.loadTexts:cficonReservedPortNumGroup.setStatus(_B)
cficonRlirErlGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,20))
cficonRlirErlGroup.setObjects((_A,_BC))
if mibBuilder.loadTexts:cficonRlirErlGroup.setStatus(_B)
cficonInterfaceSwapGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,21))
cficonInterfaceSwapGroup.setObjects(*((_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ)))
if mibBuilder.loadTexts:cficonInterfaceSwapGroup.setStatus(_B)
cficonDefaultPortBlockGroup=ObjectGroup((1,3,6,1,4,1,9,9,375,2,2,22))
cficonDefaultPortBlockGroup.setObjects((_A,_BK))
if mibBuilder.loadTexts:cficonDefaultPortBlockGroup.setStatus(_B)
cficonPortInfoChange=NotificationType((1,3,6,1,4,1,9,9,375,0,1))
cficonPortInfoChange.setObjects(*((_A,_m),(_e,_f)))
if mibBuilder.loadTexts:cficonPortInfoChange.setStatus(_B)
cficonNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,375,2,2,17))
cficonNotificationGroup.setObjects((_A,_BL))
if mibBuilder.loadTexts:cficonNotificationGroup.setStatus(_B)
ciscoFiconCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,375,2,1,1))
ciscoFiconCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_BM),(_A,_d)))
if mibBuilder.loadTexts:ciscoFiconCompliance.setStatus(_J)
ciscoFiconComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,375,2,1,2))
ciscoFiconComplianceRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoFiconComplianceRev1.setStatus(_J)
ciscoFiconComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,375,2,1,3))
ciscoFiconComplianceRev2.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_h),(_A,_i),(_A,_j),(_A,_n)))
if mibBuilder.loadTexts:ciscoFiconComplianceRev2.setStatus(_J)
ciscoFiconComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,375,2,1,4))
ciscoFiconComplianceRev3.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_h),(_A,_i),(_A,_j),(_A,_n),(_A,_BN)))
if mibBuilder.loadTexts:ciscoFiconComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CficonPortNumOrAddr':CficonPortNumOrAddr,'ciscoFiconMIB':ciscoFiconMIB,'ciscoFiconMIBNotifications':ciscoFiconMIBNotifications,_BL:cficonPortInfoChange,'ciscoFiconMIBObjects':ciscoFiconMIBObjects,'ciscoFiconConfig':ciscoFiconConfig,'cficonPortSwapTable':cficonPortSwapTable,'cficonPortSwapEntry':cficonPortSwapEntry,_o:cficonPortSwapIndex,_A4:cficonSwapPortNumberFirst,_A5:cficonSwapPortNumberSecond,_A6:cficonSwapPortEntryStatus,'cficonVsanTable':cficonVsanTable,'cficonVsanEntry':cficonVsanEntry,_A7:cficonVsanHostControl,_A8:cficonVsanHostControlSwOffline,_A9:cficonVsanHostControlClkAlrtMode,_AA:cficonVsanSnmpControl,_AB:cficonVsanAutoSavePortAddrCfg,_AC:cficonVsanEnableCup,_AD:cficonVsanCodePage,_AE:cficonVsanCharSet,_AF:cficonVsanKeyCounter,_AG:cficonVsanUserAlertMode,_AH:cficonVsanDeviceAllegience,_AI:cficonVsanTime,_AJ:cficonVsanHostOrDefaultTime,_AK:cficonVsanCupName,_AL:cficonSetHostTimeControl,_AM:cficonVsanClearAllegience,_AN:cficonVsanEntryStatus,_AO:cficonVsanFiconState,_AP:cficonVsanSerialNum,'cficonPortTable':cficonPortTable,'cficonPortEntry':cficonPortEntry,_q:cficonPortAddr,_AQ:cficonPortBlock,_AR:cficonPortName,_AS:cficonProhibitPortNumbers,'cficonPortRunCfgTable':cficonPortRunCfgTable,'cficonPortRunCfgEntry':cficonPortRunCfgEntry,_r:cficonPortRunCfgAddr,_AT:cficonPortRunCfgBlock,_AU:cficonPortRunCfgName,_AV:cficonRunCfgProhibitPrtNums,_AW:cficonRunCfgTypeNumber,_AX:cficonRunCfgModelNumber,_AY:cficonRunCfgManufacturer,_AZ:cficonRunCfgPlantOfMfg,_Aa:cficonRunCfgSerialNumber,_m:cficonRunCfgUnitType,_Ab:cficonRunCfgPortId,_Ac:cficonRunCfgStatus,'cficonCfgFileTable':cficonCfgFileTable,'cficonCfgFileEntry':cficonCfgFileEntry,_g:cficonCfgFilename,_Ad:cficonCfgFileDescr,_Ae:cficonCfgFileStatus,_Af:cficonCfgFileLastUpdated,_Ag:cficonCfgFileCmd,_Ah:cficonCfgFileRowStatus,_Ai:cficonCfgFileCmdStatus,_Aj:cficonCfgFileCmdErrorString,'cficonPortNumIfTable':cficonPortNumIfTable,'cficonPortNumIfEntry':cficonPortNumIfEntry,_u:cficonPortNumber,_Ak:cficonPortIfIndex,'cficonPortAddrNumTable':cficonPortAddrNumTable,'cficonPortAddrNumEntry':cficonPortAddrNumEntry,_v:cficonPortAddrPortAddr,_Al:cficonPortAddrPortNumber,'cficonPortNumAddrTable':cficonPortNumAddrTable,'cficonPortNumAddrEntry':cficonPortNumAddrEntry,_w:portAddrPortNumber,_Am:portAddress,'cficonDirHistTable':cficonDirHistTable,'cficonDirHistEntry':cficonDirHistEntry,_x:cficonDirHistKeyCounter,_An:cficonDirHistPortNumbers,'cficonStatsTable':cficonStatsTable,'cficonStatsEntry':cficonStatsEntry,_Ao:cfStatsFramePacingTime,_Ap:cfStatsDispErrorsInFrame,_Aq:cfStatsEOFErrs,_Ar:cfStatsDispErrsOutOfFrame,_As:cfStatsInvalidOrderSets,_At:cfStatsErrorSummary,_Au:cficonShowPorts,'cficonLinkIncidentTable':cficonLinkIncidentTable,'cficonLinkIncidentEntry':cficonLinkIncidentEntry,_Av:cficonLinkIncident,_Aw:cficonLinkIncidentTime,_Ax:cficonLinkIncidentClear,'cficonCfgFileCupNameTable':cficonCfgFileCupNameTable,'cficonCfgFileCupNameEntry':cficonCfgFileCupNameEntry,_Ay:cficonCfgFileCupName,'cficonConfigCopyTable':cficonConfigCopyTable,'cficonConfigCopyEntry':cficonConfigCopyEntry,_y:cficonConfigCopyIndex,_Az:cficonCopyState,_A_:cficonCopyFailReason,_B0:cficonCopyEntryRowStatus,_B1:cficonAutoSaveState,'ciscoFiconPortMap':ciscoFiconPortMap,_B2:cficonPortMap1,_B3:cficonPortMap2,_B4:cficonPortMap3,_B5:cficonPortMap4,_B6:cficonPortMap5,_B7:cficonPortMap6,_B8:cficonPortMapMax,'cficonPortMapTable':cficonPortMapTable,'cficonPortMapEntry':cficonPortMapEntry,_z:cficonPortMapIndex,_B9:cficonPortMapObj,'cficonSlotPortNumTable':cficonSlotPortNumTable,'cficonSlotPortNumEntry':cficonSlotPortNumEntry,_A0:cficonSlotIndex,_BA:cficonSlotReservedPN,_BB:cficonLogicReservedPN,'cficonRlirErlTable':cficonRlirErlTable,'cficonRlirErlEntry':cficonRlirErlEntry,_A1:cficonRlirErlFcId,_A2:cficonRlirErlFormat,_BC:cficonRlirErlRegType,'cficonInterfaceSwapTable':cficonInterfaceSwapTable,'cficonInterfaceSwapEntry':cficonInterfaceSwapEntry,_A3:cficonInterfaceSwapIndex,_BD:cficonSwapInterfaceIndexFirst,_BE:cficonSwapInterfaceIndexSecond,_BF:cficonSwapInterfaceActionStatus,_BG:cficonSwapInterfaceFailReason,_BH:cficonSwapInterfaceSystemError,_BI:cficonSwapInterfaceEntryStatus,_BJ:cficonInterfaceSwapNextIndex,'ciscoFiconGlobal':ciscoFiconGlobal,_BK:cficonDefaultPortBlock,'ciscoFiconMIBConform':ciscoFiconMIBConform,'ciscoFiconCompliances':ciscoFiconCompliances,'ciscoFiconCompliance':ciscoFiconCompliance,'ciscoFiconComplianceRev1':ciscoFiconComplianceRev1,'ciscoFiconComplianceRev2':ciscoFiconComplianceRev2,'ciscoFiconComplianceRev3':ciscoFiconComplianceRev3,'ciscoFiconGroups':ciscoFiconGroups,_O:cficonPortSwapGroup,_P:cficonVsanGroup,_Q:cficonPortGroup,_R:cficonPortRunCfgGroup,_S:cficonCfgFileGroup,_T:cficonPortNumIfGroup,_U:cficonPortAddrNumGroup,_V:cficonPortNumAddrGroup,_W:cficonDirHistGroup,_X:cficonStatsGroup,_Y:cifconShowPortGroup,_Z:cficonLinkIncidentGroup,_a:cficonCfgFileCupNameGroup,_b:cficonConfigCopyGroup,_c:cficonAutoSaveStateGroup,_BM:cficonPortMapGroup,_d:cficonNotificationGroup,_h:cficonPortMapGroupRev1,_i:cficonReservedPortNumGroup,_j:cficonRlirErlGroup,_n:cficonInterfaceSwapGroup,_BN:cficonDefaultPortBlockGroup})