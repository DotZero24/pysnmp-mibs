_v='ciscoEnhancedWredGroup'
_u='cewredRxMulticastRowStatus'
_t='cewredRxMulticastValue'
_s='cewredRxRowStatus'
_r='cewredRxValue'
_q='cewredRxIfRowStatus'
_p='cewredRxIfValue'
_o='cewredTxRowStatus'
_n='cewredTxValue'
_m='cewredConfigRedProfile'
_l='cewredConfigGlobCosGroupName'
_k='cewredStatSwitchedPkts64'
_j='cewredStatSwitchedPkts'
_i='cewredQueueParamMaxDepth'
_h='cewredQueueParamDepth'
_g='cewredQueueParamMaxAverage'
_f='cewredQueueParamWeight'
_e='cewredConfigRedQueueNumber'
_d='cewredStatMaxFilteredPkts64'
_c='cewredStatRandomFilteredPkts64'
_b='cewredStatMaxFilteredPkts'
_a='cewredStatRandomFilteredPkts'
_Z='cewredQueueParamAverage'
_Y='cewredConfigRedRowStatus'
_X='cewredConfigRedPktsDropFract'
_W='cewredConfigRedMaxThreshold'
_V='cewredConfigRedMinThreshold'
_U='cewredConfigGlobRowStatus'
_T='cewredConfigGlobDscpPrec'
_S='cewredConfigGlobQueueWeight'
_R='cewredStatRedProfile'
_Q='cewredQueueParamNumber'
_P='cewredConfigRedValue'
_O='cewredRxDestId'
_N='cewredRxSourceId'
_M='SnmpAdminString'
_L='read-write'
_K='ifIndex'
_J='IF-MIB'
_I='entPhysicalIndex'
_H='ENTITY-MIB'
_G='cewredConfigGlobIndex'
_F='not-accessible'
_E='read-only'
_D='packets'
_C='read-create'
_B='CISCO-ENHANCED-WRED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_H,'PhysicalIndex',_I)
ifIndex,=mibBuilder.importSymbols(_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoEnhancedWredMIB=ModuleIdentity((1,3,6,1,4,1,9,9,222))
if mibBuilder.loadTexts:ciscoEnhancedWredMIB.setRevisions(('2001-12-21 00:00',))
class CewredQueueNumber(TextualConvention,Unsigned32):status=_A
class CewredRedMechanism(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('precedence',1),('dscp',2)))
class CewredRedProfile(TextualConvention,Unsigned32):status=_A
class CewredIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CewredMIBNotifications_ObjectIdentity=ObjectIdentity
cewredMIBNotifications=_CewredMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,222,0))
_CiscoEnhancedWredMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEnhancedWredMIBObjects=_CiscoEnhancedWredMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,222,1))
_CewredTx_ObjectIdentity=ObjectIdentity
cewredTx=_CewredTx_ObjectIdentity((1,3,6,1,4,1,9,9,222,1,1))
_CewredTxTable_Object=MibTable
cewredTxTable=_CewredTxTable_Object((1,3,6,1,4,1,9,9,222,1,1,1))
if mibBuilder.loadTexts:cewredTxTable.setStatus(_A)
_CewredTxEntry_Object=MibTableRow
cewredTxEntry=_CewredTxEntry_Object((1,3,6,1,4,1,9,9,222,1,1,1,1))
cewredTxEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cewredTxEntry.setStatus(_A)
_CewredTxValue_Type=CewredIndex
_CewredTxValue_Object=MibTableColumn
cewredTxValue=_CewredTxValue_Object((1,3,6,1,4,1,9,9,222,1,1,1,1,1),_CewredTxValue_Type())
cewredTxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredTxValue.setStatus(_A)
_CewredTxRowStatus_Type=RowStatus
_CewredTxRowStatus_Object=MibTableColumn
cewredTxRowStatus=_CewredTxRowStatus_Object((1,3,6,1,4,1,9,9,222,1,1,1,1,2),_CewredTxRowStatus_Type())
cewredTxRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredTxRowStatus.setStatus(_A)
_CewredRx_ObjectIdentity=ObjectIdentity
cewredRx=_CewredRx_ObjectIdentity((1,3,6,1,4,1,9,9,222,1,2))
_CewredRxIfTable_Object=MibTable
cewredRxIfTable=_CewredRxIfTable_Object((1,3,6,1,4,1,9,9,222,1,2,1))
if mibBuilder.loadTexts:cewredRxIfTable.setStatus(_A)
_CewredRxIfEntry_Object=MibTableRow
cewredRxIfEntry=_CewredRxIfEntry_Object((1,3,6,1,4,1,9,9,222,1,2,1,1))
cewredRxIfEntry.setIndexNames((0,_H,_I),(0,_J,_K))
if mibBuilder.loadTexts:cewredRxIfEntry.setStatus(_A)
_CewredRxIfValue_Type=CewredIndex
_CewredRxIfValue_Object=MibTableColumn
cewredRxIfValue=_CewredRxIfValue_Object((1,3,6,1,4,1,9,9,222,1,2,1,1,1),_CewredRxIfValue_Type())
cewredRxIfValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredRxIfValue.setStatus(_A)
_CewredRxIfRowStatus_Type=RowStatus
_CewredRxIfRowStatus_Object=MibTableColumn
cewredRxIfRowStatus=_CewredRxIfRowStatus_Object((1,3,6,1,4,1,9,9,222,1,2,1,1,2),_CewredRxIfRowStatus_Type())
cewredRxIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredRxIfRowStatus.setStatus(_A)
_CewredRxTable_Object=MibTable
cewredRxTable=_CewredRxTable_Object((1,3,6,1,4,1,9,9,222,1,2,2))
if mibBuilder.loadTexts:cewredRxTable.setStatus(_A)
_CewredRxEntry_Object=MibTableRow
cewredRxEntry=_CewredRxEntry_Object((1,3,6,1,4,1,9,9,222,1,2,2,1))
cewredRxEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:cewredRxEntry.setStatus(_A)
_CewredRxSourceId_Type=PhysicalIndex
_CewredRxSourceId_Object=MibTableColumn
cewredRxSourceId=_CewredRxSourceId_Object((1,3,6,1,4,1,9,9,222,1,2,2,1,1),_CewredRxSourceId_Type())
cewredRxSourceId.setMaxAccess(_F)
if mibBuilder.loadTexts:cewredRxSourceId.setStatus(_A)
_CewredRxDestId_Type=PhysicalIndex
_CewredRxDestId_Object=MibTableColumn
cewredRxDestId=_CewredRxDestId_Object((1,3,6,1,4,1,9,9,222,1,2,2,1,2),_CewredRxDestId_Type())
cewredRxDestId.setMaxAccess(_F)
if mibBuilder.loadTexts:cewredRxDestId.setStatus(_A)
_CewredRxValue_Type=CewredIndex
_CewredRxValue_Object=MibTableColumn
cewredRxValue=_CewredRxValue_Object((1,3,6,1,4,1,9,9,222,1,2,2,1,3),_CewredRxValue_Type())
cewredRxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredRxValue.setStatus(_A)
_CewredRxRowStatus_Type=RowStatus
_CewredRxRowStatus_Object=MibTableColumn
cewredRxRowStatus=_CewredRxRowStatus_Object((1,3,6,1,4,1,9,9,222,1,2,2,1,4),_CewredRxRowStatus_Type())
cewredRxRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredRxRowStatus.setStatus(_A)
_CewredRxMulticastTable_Object=MibTable
cewredRxMulticastTable=_CewredRxMulticastTable_Object((1,3,6,1,4,1,9,9,222,1,2,3))
if mibBuilder.loadTexts:cewredRxMulticastTable.setStatus(_A)
_CewredRxMulticastEntry_Object=MibTableRow
cewredRxMulticastEntry=_CewredRxMulticastEntry_Object((1,3,6,1,4,1,9,9,222,1,2,3,1))
cewredRxMulticastEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cewredRxMulticastEntry.setStatus(_A)
_CewredRxMulticastValue_Type=CewredIndex
_CewredRxMulticastValue_Object=MibTableColumn
cewredRxMulticastValue=_CewredRxMulticastValue_Object((1,3,6,1,4,1,9,9,222,1,2,3,1,1),_CewredRxMulticastValue_Type())
cewredRxMulticastValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredRxMulticastValue.setStatus(_A)
_CewredRxMulticastRowStatus_Type=RowStatus
_CewredRxMulticastRowStatus_Object=MibTableColumn
cewredRxMulticastRowStatus=_CewredRxMulticastRowStatus_Object((1,3,6,1,4,1,9,9,222,1,2,3,1,2),_CewredRxMulticastRowStatus_Type())
cewredRxMulticastRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredRxMulticastRowStatus.setStatus(_A)
_CewredConfig_ObjectIdentity=ObjectIdentity
cewredConfig=_CewredConfig_ObjectIdentity((1,3,6,1,4,1,9,9,222,1,3))
_CewredConfigGlobTable_Object=MibTable
cewredConfigGlobTable=_CewredConfigGlobTable_Object((1,3,6,1,4,1,9,9,222,1,3,1))
if mibBuilder.loadTexts:cewredConfigGlobTable.setStatus(_A)
_CewredConfigGlobEntry_Object=MibTableRow
cewredConfigGlobEntry=_CewredConfigGlobEntry_Object((1,3,6,1,4,1,9,9,222,1,3,1,1))
cewredConfigGlobEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cewredConfigGlobEntry.setStatus(_A)
_CewredConfigGlobIndex_Type=CewredIndex
_CewredConfigGlobIndex_Object=MibTableColumn
cewredConfigGlobIndex=_CewredConfigGlobIndex_Object((1,3,6,1,4,1,9,9,222,1,3,1,1,1),_CewredConfigGlobIndex_Type())
cewredConfigGlobIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cewredConfigGlobIndex.setStatus(_A)
class _CewredConfigGlobCosGroupName_Type(SnmpAdminString):defaultValue=OctetString('')
_CewredConfigGlobCosGroupName_Type.__name__=_M
_CewredConfigGlobCosGroupName_Object=MibTableColumn
cewredConfigGlobCosGroupName=_CewredConfigGlobCosGroupName_Object((1,3,6,1,4,1,9,9,222,1,3,1,1,2),_CewredConfigGlobCosGroupName_Type())
cewredConfigGlobCosGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigGlobCosGroupName.setStatus(_A)
_CewredConfigGlobQueueWeight_Type=Unsigned32
_CewredConfigGlobQueueWeight_Object=MibTableColumn
cewredConfigGlobQueueWeight=_CewredConfigGlobQueueWeight_Object((1,3,6,1,4,1,9,9,222,1,3,1,1,3),_CewredConfigGlobQueueWeight_Type())
cewredConfigGlobQueueWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigGlobQueueWeight.setStatus(_A)
_CewredConfigGlobDscpPrec_Type=CewredRedMechanism
_CewredConfigGlobDscpPrec_Object=MibTableColumn
cewredConfigGlobDscpPrec=_CewredConfigGlobDscpPrec_Object((1,3,6,1,4,1,9,9,222,1,3,1,1,4),_CewredConfigGlobDscpPrec_Type())
cewredConfigGlobDscpPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigGlobDscpPrec.setStatus(_A)
_CewredConfigGlobRowStatus_Type=RowStatus
_CewredConfigGlobRowStatus_Object=MibTableColumn
cewredConfigGlobRowStatus=_CewredConfigGlobRowStatus_Object((1,3,6,1,4,1,9,9,222,1,3,1,1,5),_CewredConfigGlobRowStatus_Type())
cewredConfigGlobRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigGlobRowStatus.setStatus(_A)
_CewredConfigRedTable_Object=MibTable
cewredConfigRedTable=_CewredConfigRedTable_Object((1,3,6,1,4,1,9,9,222,1,3,2))
if mibBuilder.loadTexts:cewredConfigRedTable.setStatus(_A)
_CewredConfigRedEntry_Object=MibTableRow
cewredConfigRedEntry=_CewredConfigRedEntry_Object((1,3,6,1,4,1,9,9,222,1,3,2,1))
cewredConfigRedEntry.setIndexNames((0,_B,_G),(0,_B,_P))
if mibBuilder.loadTexts:cewredConfigRedEntry.setStatus(_A)
_CewredConfigRedValue_Type=Unsigned32
_CewredConfigRedValue_Object=MibTableColumn
cewredConfigRedValue=_CewredConfigRedValue_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,1),_CewredConfigRedValue_Type())
cewredConfigRedValue.setMaxAccess(_F)
if mibBuilder.loadTexts:cewredConfigRedValue.setStatus(_A)
_CewredConfigRedQueueNumber_Type=CewredQueueNumber
_CewredConfigRedQueueNumber_Object=MibTableColumn
cewredConfigRedQueueNumber=_CewredConfigRedQueueNumber_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,2),_CewredConfigRedQueueNumber_Type())
cewredConfigRedQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigRedQueueNumber.setStatus(_A)
_CewredConfigRedProfile_Type=CewredRedProfile
_CewredConfigRedProfile_Object=MibTableColumn
cewredConfigRedProfile=_CewredConfigRedProfile_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,3),_CewredConfigRedProfile_Type())
cewredConfigRedProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigRedProfile.setStatus(_A)
_CewredConfigRedMinThreshold_Type=Unsigned32
_CewredConfigRedMinThreshold_Object=MibTableColumn
cewredConfigRedMinThreshold=_CewredConfigRedMinThreshold_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,4),_CewredConfigRedMinThreshold_Type())
cewredConfigRedMinThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigRedMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:cewredConfigRedMinThreshold.setUnits(_D)
_CewredConfigRedMaxThreshold_Type=Unsigned32
_CewredConfigRedMaxThreshold_Object=MibTableColumn
cewredConfigRedMaxThreshold=_CewredConfigRedMaxThreshold_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,5),_CewredConfigRedMaxThreshold_Type())
cewredConfigRedMaxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigRedMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:cewredConfigRedMaxThreshold.setUnits(_D)
_CewredConfigRedPktsDropFract_Type=Unsigned32
_CewredConfigRedPktsDropFract_Object=MibTableColumn
cewredConfigRedPktsDropFract=_CewredConfigRedPktsDropFract_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,6),_CewredConfigRedPktsDropFract_Type())
cewredConfigRedPktsDropFract.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigRedPktsDropFract.setStatus(_A)
_CewredConfigRedRowStatus_Type=RowStatus
_CewredConfigRedRowStatus_Object=MibTableColumn
cewredConfigRedRowStatus=_CewredConfigRedRowStatus_Object((1,3,6,1,4,1,9,9,222,1,3,2,1,7),_CewredConfigRedRowStatus_Type())
cewredConfigRedRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cewredConfigRedRowStatus.setStatus(_A)
_CewredQueue_ObjectIdentity=ObjectIdentity
cewredQueue=_CewredQueue_ObjectIdentity((1,3,6,1,4,1,9,9,222,1,4))
_CewredQueueParamTable_Object=MibTable
cewredQueueParamTable=_CewredQueueParamTable_Object((1,3,6,1,4,1,9,9,222,1,4,1))
if mibBuilder.loadTexts:cewredQueueParamTable.setStatus(_A)
_CewredQueueParamEntry_Object=MibTableRow
cewredQueueParamEntry=_CewredQueueParamEntry_Object((1,3,6,1,4,1,9,9,222,1,4,1,1))
cewredQueueParamEntry.setIndexNames((0,_B,_G),(0,_B,_Q))
if mibBuilder.loadTexts:cewredQueueParamEntry.setStatus(_A)
_CewredQueueParamNumber_Type=CewredQueueNumber
_CewredQueueParamNumber_Object=MibTableColumn
cewredQueueParamNumber=_CewredQueueParamNumber_Object((1,3,6,1,4,1,9,9,222,1,4,1,1,1),_CewredQueueParamNumber_Type())
cewredQueueParamNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:cewredQueueParamNumber.setStatus(_A)
_CewredQueueParamWeight_Type=Unsigned32
_CewredQueueParamWeight_Object=MibTableColumn
cewredQueueParamWeight=_CewredQueueParamWeight_Object((1,3,6,1,4,1,9,9,222,1,4,1,1,2),_CewredQueueParamWeight_Type())
cewredQueueParamWeight.setMaxAccess(_L)
if mibBuilder.loadTexts:cewredQueueParamWeight.setStatus(_A)
_CewredQueueParamAverage_Type=Gauge32
_CewredQueueParamAverage_Object=MibTableColumn
cewredQueueParamAverage=_CewredQueueParamAverage_Object((1,3,6,1,4,1,9,9,222,1,4,1,1,3),_CewredQueueParamAverage_Type())
cewredQueueParamAverage.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredQueueParamAverage.setStatus(_A)
if mibBuilder.loadTexts:cewredQueueParamAverage.setUnits(_D)
_CewredQueueParamMaxAverage_Type=Gauge32
_CewredQueueParamMaxAverage_Object=MibTableColumn
cewredQueueParamMaxAverage=_CewredQueueParamMaxAverage_Object((1,3,6,1,4,1,9,9,222,1,4,1,1,4),_CewredQueueParamMaxAverage_Type())
cewredQueueParamMaxAverage.setMaxAccess(_L)
if mibBuilder.loadTexts:cewredQueueParamMaxAverage.setStatus(_A)
if mibBuilder.loadTexts:cewredQueueParamMaxAverage.setUnits(_D)
_CewredQueueParamDepth_Type=Gauge32
_CewredQueueParamDepth_Object=MibTableColumn
cewredQueueParamDepth=_CewredQueueParamDepth_Object((1,3,6,1,4,1,9,9,222,1,4,1,1,5),_CewredQueueParamDepth_Type())
cewredQueueParamDepth.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredQueueParamDepth.setStatus(_A)
if mibBuilder.loadTexts:cewredQueueParamDepth.setUnits(_D)
_CewredQueueParamMaxDepth_Type=Gauge32
_CewredQueueParamMaxDepth_Object=MibTableColumn
cewredQueueParamMaxDepth=_CewredQueueParamMaxDepth_Object((1,3,6,1,4,1,9,9,222,1,4,1,1,6),_CewredQueueParamMaxDepth_Type())
cewredQueueParamMaxDepth.setMaxAccess(_L)
if mibBuilder.loadTexts:cewredQueueParamMaxDepth.setStatus(_A)
if mibBuilder.loadTexts:cewredQueueParamMaxDepth.setUnits(_D)
_CewredStat_ObjectIdentity=ObjectIdentity
cewredStat=_CewredStat_ObjectIdentity((1,3,6,1,4,1,9,9,222,1,5))
_CewredStatTable_Object=MibTable
cewredStatTable=_CewredStatTable_Object((1,3,6,1,4,1,9,9,222,1,5,1))
if mibBuilder.loadTexts:cewredStatTable.setStatus(_A)
_CewredStatEntry_Object=MibTableRow
cewredStatEntry=_CewredStatEntry_Object((1,3,6,1,4,1,9,9,222,1,5,1,1))
cewredStatEntry.setIndexNames((0,_B,_G),(0,_B,_R))
if mibBuilder.loadTexts:cewredStatEntry.setStatus(_A)
_CewredStatRedProfile_Type=CewredRedProfile
_CewredStatRedProfile_Object=MibTableColumn
cewredStatRedProfile=_CewredStatRedProfile_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,1),_CewredStatRedProfile_Type())
cewredStatRedProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:cewredStatRedProfile.setStatus(_A)
_CewredStatSwitchedPkts_Type=Counter32
_CewredStatSwitchedPkts_Object=MibTableColumn
cewredStatSwitchedPkts=_CewredStatSwitchedPkts_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,2),_CewredStatSwitchedPkts_Type())
cewredStatSwitchedPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredStatSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:cewredStatSwitchedPkts.setUnits(_D)
_CewredStatRandomFilteredPkts_Type=Counter32
_CewredStatRandomFilteredPkts_Object=MibTableColumn
cewredStatRandomFilteredPkts=_CewredStatRandomFilteredPkts_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,3),_CewredStatRandomFilteredPkts_Type())
cewredStatRandomFilteredPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredStatRandomFilteredPkts.setStatus(_A)
if mibBuilder.loadTexts:cewredStatRandomFilteredPkts.setUnits(_D)
_CewredStatMaxFilteredPkts_Type=Counter32
_CewredStatMaxFilteredPkts_Object=MibTableColumn
cewredStatMaxFilteredPkts=_CewredStatMaxFilteredPkts_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,4),_CewredStatMaxFilteredPkts_Type())
cewredStatMaxFilteredPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredStatMaxFilteredPkts.setStatus(_A)
if mibBuilder.loadTexts:cewredStatMaxFilteredPkts.setUnits(_D)
_CewredStatSwitchedPkts64_Type=Counter64
_CewredStatSwitchedPkts64_Object=MibTableColumn
cewredStatSwitchedPkts64=_CewredStatSwitchedPkts64_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,5),_CewredStatSwitchedPkts64_Type())
cewredStatSwitchedPkts64.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredStatSwitchedPkts64.setStatus(_A)
if mibBuilder.loadTexts:cewredStatSwitchedPkts64.setUnits(_D)
_CewredStatRandomFilteredPkts64_Type=Counter64
_CewredStatRandomFilteredPkts64_Object=MibTableColumn
cewredStatRandomFilteredPkts64=_CewredStatRandomFilteredPkts64_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,6),_CewredStatRandomFilteredPkts64_Type())
cewredStatRandomFilteredPkts64.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredStatRandomFilteredPkts64.setStatus(_A)
if mibBuilder.loadTexts:cewredStatRandomFilteredPkts64.setUnits(_D)
_CewredStatMaxFilteredPkts64_Type=Counter64
_CewredStatMaxFilteredPkts64_Object=MibTableColumn
cewredStatMaxFilteredPkts64=_CewredStatMaxFilteredPkts64_Object((1,3,6,1,4,1,9,9,222,1,5,1,1,7),_CewredStatMaxFilteredPkts64_Type())
cewredStatMaxFilteredPkts64.setMaxAccess(_E)
if mibBuilder.loadTexts:cewredStatMaxFilteredPkts64.setStatus(_A)
if mibBuilder.loadTexts:cewredStatMaxFilteredPkts64.setUnits(_D)
_CewredMIBConformance_ObjectIdentity=ObjectIdentity
cewredMIBConformance=_CewredMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,222,3))
_CewredMIBCompliances_ObjectIdentity=ObjectIdentity
cewredMIBCompliances=_CewredMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,222,3,1))
_CewredMIBGroups_ObjectIdentity=ObjectIdentity
cewredMIBGroups=_CewredMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,222,3,2))
ciscoEnhancedWredGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,1))
ciscoEnhancedWredGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoEnhancedWredGroup.setStatus(_A)
ciscoEnhancedWredDrrQueueGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,2))
ciscoEnhancedWredDrrQueueGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ciscoEnhancedWredDrrQueueGroup.setStatus(_A)
ciscoEnhancedWredStatCountGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,3))
ciscoEnhancedWredStatCountGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoEnhancedWredStatCountGroup.setStatus(_A)
ciscoEnhancedWredCosQueueGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,4))
ciscoEnhancedWredCosQueueGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ciscoEnhancedWredCosQueueGroup.setStatus(_A)
ciscoEnhancedWredTxInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,5))
ciscoEnhancedWredTxInfoGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoEnhancedWredTxInfoGroup.setStatus(_A)
ciscoEnhancedWredRxIfInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,6))
ciscoEnhancedWredRxIfInfoGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoEnhancedWredRxIfInfoGroup.setStatus(_A)
ciscoEnhancedWredRxInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,7))
ciscoEnhancedWredRxInfoGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ciscoEnhancedWredRxInfoGroup.setStatus(_A)
ciscoEnhancedWredRxMcInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,222,3,2,8))
ciscoEnhancedWredRxMcInfoGroup.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoEnhancedWredRxMcInfoGroup.setStatus(_A)
cewredMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,222,3,1,1))
cewredMIBCompliance.setObjects((_B,_v))
if mibBuilder.loadTexts:cewredMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CewredQueueNumber':CewredQueueNumber,'CewredRedMechanism':CewredRedMechanism,'CewredRedProfile':CewredRedProfile,'CewredIndex':CewredIndex,'ciscoEnhancedWredMIB':ciscoEnhancedWredMIB,'cewredMIBNotifications':cewredMIBNotifications,'ciscoEnhancedWredMIBObjects':ciscoEnhancedWredMIBObjects,'cewredTx':cewredTx,'cewredTxTable':cewredTxTable,'cewredTxEntry':cewredTxEntry,_n:cewredTxValue,_o:cewredTxRowStatus,'cewredRx':cewredRx,'cewredRxIfTable':cewredRxIfTable,'cewredRxIfEntry':cewredRxIfEntry,_p:cewredRxIfValue,_q:cewredRxIfRowStatus,'cewredRxTable':cewredRxTable,'cewredRxEntry':cewredRxEntry,_N:cewredRxSourceId,_O:cewredRxDestId,_r:cewredRxValue,_s:cewredRxRowStatus,'cewredRxMulticastTable':cewredRxMulticastTable,'cewredRxMulticastEntry':cewredRxMulticastEntry,_t:cewredRxMulticastValue,_u:cewredRxMulticastRowStatus,'cewredConfig':cewredConfig,'cewredConfigGlobTable':cewredConfigGlobTable,'cewredConfigGlobEntry':cewredConfigGlobEntry,_G:cewredConfigGlobIndex,_l:cewredConfigGlobCosGroupName,_S:cewredConfigGlobQueueWeight,_T:cewredConfigGlobDscpPrec,_U:cewredConfigGlobRowStatus,'cewredConfigRedTable':cewredConfigRedTable,'cewredConfigRedEntry':cewredConfigRedEntry,_P:cewredConfigRedValue,_e:cewredConfigRedQueueNumber,_m:cewredConfigRedProfile,_V:cewredConfigRedMinThreshold,_W:cewredConfigRedMaxThreshold,_X:cewredConfigRedPktsDropFract,_Y:cewredConfigRedRowStatus,'cewredQueue':cewredQueue,'cewredQueueParamTable':cewredQueueParamTable,'cewredQueueParamEntry':cewredQueueParamEntry,_Q:cewredQueueParamNumber,_f:cewredQueueParamWeight,_Z:cewredQueueParamAverage,_g:cewredQueueParamMaxAverage,_h:cewredQueueParamDepth,_i:cewredQueueParamMaxDepth,'cewredStat':cewredStat,'cewredStatTable':cewredStatTable,'cewredStatEntry':cewredStatEntry,_R:cewredStatRedProfile,_j:cewredStatSwitchedPkts,_a:cewredStatRandomFilteredPkts,_b:cewredStatMaxFilteredPkts,_k:cewredStatSwitchedPkts64,_c:cewredStatRandomFilteredPkts64,_d:cewredStatMaxFilteredPkts64,'cewredMIBConformance':cewredMIBConformance,'cewredMIBCompliances':cewredMIBCompliances,'cewredMIBCompliance':cewredMIBCompliance,'cewredMIBGroups':cewredMIBGroups,_v:ciscoEnhancedWredGroup,'ciscoEnhancedWredDrrQueueGroup':ciscoEnhancedWredDrrQueueGroup,'ciscoEnhancedWredStatCountGroup':ciscoEnhancedWredStatCountGroup,'ciscoEnhancedWredCosQueueGroup':ciscoEnhancedWredCosQueueGroup,'ciscoEnhancedWredTxInfoGroup':ciscoEnhancedWredTxInfoGroup,'ciscoEnhancedWredRxIfInfoGroup':ciscoEnhancedWredRxIfInfoGroup,'ciscoEnhancedWredRxInfoGroup':ciscoEnhancedWredRxInfoGroup,'ciscoEnhancedWredRxMcInfoGroup':ciscoEnhancedWredRxMcInfoGroup})