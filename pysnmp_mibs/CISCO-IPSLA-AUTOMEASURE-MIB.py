_A1='ciscoIpSlaAutoGroupSchedGroup'
_A0='ciscoIpSlaAutoGroupReactGroup'
_z='ciscoIpSlaAutoGroupDestGroup'
_y='ciscoIpSlaAutoGroupConfGroup'
_x='cipslaAutoGroupSchedRowStatus'
_w='cipslaAutoGroupSchedStorageType'
_v='cipslaAutoGroupSchedStartTime'
_u='cipslaAutoGroupSchedMinInterval'
_t='cipslaAutoGroupSchedMaxInterval'
_s='cipslaAutoGroupSchedAgeout'
_r='cipslaAutoGroupSchedLife'
_q='cipslaAutoGroupSchedInterval'
_p='cipslaAutoGroupSchedPeriod'
_o='cipslaReactRowStatus'
_n='cipslaReactStorageType'
_m='cipslaReactThresholdCountY'
_l='cipslaReactThresholdCountX'
_k='cipslaReactThresholdFalling'
_j='cipslaReactThresholdRising'
_i='cipslaReactActionType'
_h='cipslaReactThresholdType'
_g='cipslaReactVar'
_f='cipslaAutoGroupDestRowStatus'
_e='cipslaAutoGroupDestStorageType'
_d='cipslaAutoGroupRowStatus'
_c='cipslaAutoGroupStorageType'
_b='cipslaAutoGroupADDestIPAgeout'
_a='cipslaAutoGroupADMeasureRetry'
_Z='cipslaAutoGroupDestIPADEnable'
_Y='cipslaAutoGroupQoSEnable'
_X='cipslaAutoGroupSchedulerId'
_W='cipslaAutoGroupADDestPort'
_V='cipslaAutoGroupDestinationName'
_U='cipslaAutoGroupDescription'
_T='cipslaAutoGroupSchedId'
_S='cipslaReactConfigIndex'
_R='cipslaAutoGroupDestPort'
_Q='cipslaAutoGroupDestIpAddr'
_P='cipslaAutoGroupDestIpAddrType'
_O='cipslaAutoGroupDestName'
_N='cipslaAutoGroupName'
_M='InetPortNumber'
_L='cipslaAutoGroupOperTemplateName'
_K='cipslaAutoGroupOperType'
_J='TruthValue'
_I='Integer32'
_H='StorageType'
_G='not-accessible'
_F='seconds'
_E='SnmpAdminString'
_D='Unsigned32'
_C='read-create'
_B='CISCO-IPSLA-AUTOMEASURE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IpSlaOperType,IpSlaReactVar=mibBuilder.importSymbols('CISCO-IPSLA-TC-MIB','IpSlaOperType','IpSlaReactVar')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention',_J)
ciscoIpSlaAutoMIB=ModuleIdentity((1,3,6,1,4,1,9,9,633))
if mibBuilder.loadTexts:ciscoIpSlaAutoMIB.setRevisions(('2007-06-13 00:00',))
_CiscoIpSlaAutoMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpSlaAutoMIBNotifs=_CiscoIpSlaAutoMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,633,0))
_CiscoIpSlaAutoMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpSlaAutoMIBObjects=_CiscoIpSlaAutoMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,633,1))
_CipslaAutoGroupTable_Object=MibTable
cipslaAutoGroupTable=_CipslaAutoGroupTable_Object((1,3,6,1,4,1,9,9,633,1,1))
if mibBuilder.loadTexts:cipslaAutoGroupTable.setStatus(_A)
_CipslaAutoGroupEntry_Object=MibTableRow
cipslaAutoGroupEntry=_CipslaAutoGroupEntry_Object((1,3,6,1,4,1,9,9,633,1,1,1))
cipslaAutoGroupEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cipslaAutoGroupEntry.setStatus(_A)
class _CipslaAutoGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaAutoGroupName_Type.__name__=_E
_CipslaAutoGroupName_Object=MibTableColumn
cipslaAutoGroupName=_CipslaAutoGroupName_Object((1,3,6,1,4,1,9,9,633,1,1,1,1),_CipslaAutoGroupName_Type())
cipslaAutoGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaAutoGroupName.setStatus(_A)
class _CipslaAutoGroupDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CipslaAutoGroupDescription_Type.__name__=_E
_CipslaAutoGroupDescription_Object=MibTableColumn
cipslaAutoGroupDescription=_CipslaAutoGroupDescription_Object((1,3,6,1,4,1,9,9,633,1,1,1,2),_CipslaAutoGroupDescription_Type())
cipslaAutoGroupDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupDescription.setStatus(_A)
class _CipslaAutoGroupDestinationName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CipslaAutoGroupDestinationName_Type.__name__=_E
_CipslaAutoGroupDestinationName_Object=MibTableColumn
cipslaAutoGroupDestinationName=_CipslaAutoGroupDestinationName_Object((1,3,6,1,4,1,9,9,633,1,1,1,3),_CipslaAutoGroupDestinationName_Type())
cipslaAutoGroupDestinationName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupDestinationName.setStatus(_A)
class _CipslaAutoGroupADDestPort_Type(InetPortNumber):defaultValue=0
_CipslaAutoGroupADDestPort_Type.__name__=_M
_CipslaAutoGroupADDestPort_Object=MibTableColumn
cipslaAutoGroupADDestPort=_CipslaAutoGroupADDestPort_Object((1,3,6,1,4,1,9,9,633,1,1,1,4),_CipslaAutoGroupADDestPort_Type())
cipslaAutoGroupADDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupADDestPort.setStatus(_A)
class _CipslaAutoGroupOperTemplateName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CipslaAutoGroupOperTemplateName_Type.__name__=_E
_CipslaAutoGroupOperTemplateName_Object=MibTableColumn
cipslaAutoGroupOperTemplateName=_CipslaAutoGroupOperTemplateName_Object((1,3,6,1,4,1,9,9,633,1,1,1,5),_CipslaAutoGroupOperTemplateName_Type())
cipslaAutoGroupOperTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupOperTemplateName.setStatus(_A)
class _CipslaAutoGroupSchedulerId_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CipslaAutoGroupSchedulerId_Type.__name__=_E
_CipslaAutoGroupSchedulerId_Object=MibTableColumn
cipslaAutoGroupSchedulerId=_CipslaAutoGroupSchedulerId_Object((1,3,6,1,4,1,9,9,633,1,1,1,6),_CipslaAutoGroupSchedulerId_Type())
cipslaAutoGroupSchedulerId.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedulerId.setStatus(_A)
class _CipslaAutoGroupQoSEnable_Type(TruthValue):defaultValue=2
_CipslaAutoGroupQoSEnable_Type.__name__=_J
_CipslaAutoGroupQoSEnable_Object=MibTableColumn
cipslaAutoGroupQoSEnable=_CipslaAutoGroupQoSEnable_Object((1,3,6,1,4,1,9,9,633,1,1,1,7),_CipslaAutoGroupQoSEnable_Type())
cipslaAutoGroupQoSEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupQoSEnable.setStatus(_A)
_CipslaAutoGroupOperType_Type=IpSlaOperType
_CipslaAutoGroupOperType_Object=MibTableColumn
cipslaAutoGroupOperType=_CipslaAutoGroupOperType_Object((1,3,6,1,4,1,9,9,633,1,1,1,8),_CipslaAutoGroupOperType_Type())
cipslaAutoGroupOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupOperType.setStatus(_A)
class _CipslaAutoGroupDestIPADEnable_Type(TruthValue):defaultValue=2
_CipslaAutoGroupDestIPADEnable_Type.__name__=_J
_CipslaAutoGroupDestIPADEnable_Object=MibTableColumn
cipslaAutoGroupDestIPADEnable=_CipslaAutoGroupDestIPADEnable_Object((1,3,6,1,4,1,9,9,633,1,1,1,9),_CipslaAutoGroupDestIPADEnable_Type())
cipslaAutoGroupDestIPADEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupDestIPADEnable.setStatus(_A)
class _CipslaAutoGroupADMeasureRetry_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_CipslaAutoGroupADMeasureRetry_Type.__name__=_D
_CipslaAutoGroupADMeasureRetry_Object=MibTableColumn
cipslaAutoGroupADMeasureRetry=_CipslaAutoGroupADMeasureRetry_Object((1,3,6,1,4,1,9,9,633,1,1,1,10),_CipslaAutoGroupADMeasureRetry_Type())
cipslaAutoGroupADMeasureRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupADMeasureRetry.setStatus(_A)
class _CipslaAutoGroupADDestIPAgeout_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CipslaAutoGroupADDestIPAgeout_Type.__name__=_D
_CipslaAutoGroupADDestIPAgeout_Object=MibTableColumn
cipslaAutoGroupADDestIPAgeout=_CipslaAutoGroupADDestIPAgeout_Object((1,3,6,1,4,1,9,9,633,1,1,1,11),_CipslaAutoGroupADDestIPAgeout_Type())
cipslaAutoGroupADDestIPAgeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupADDestIPAgeout.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupADDestIPAgeout.setUnits(_F)
class _CipslaAutoGroupStorageType_Type(StorageType):defaultValue=3
_CipslaAutoGroupStorageType_Type.__name__=_H
_CipslaAutoGroupStorageType_Object=MibTableColumn
cipslaAutoGroupStorageType=_CipslaAutoGroupStorageType_Object((1,3,6,1,4,1,9,9,633,1,1,1,12),_CipslaAutoGroupStorageType_Type())
cipslaAutoGroupStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupStorageType.setStatus(_A)
_CipslaAutoGroupRowStatus_Type=RowStatus
_CipslaAutoGroupRowStatus_Object=MibTableColumn
cipslaAutoGroupRowStatus=_CipslaAutoGroupRowStatus_Object((1,3,6,1,4,1,9,9,633,1,1,1,13),_CipslaAutoGroupRowStatus_Type())
cipslaAutoGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupRowStatus.setStatus(_A)
_CipslaAutoGroupDestTable_Object=MibTable
cipslaAutoGroupDestTable=_CipslaAutoGroupDestTable_Object((1,3,6,1,4,1,9,9,633,1,2))
if mibBuilder.loadTexts:cipslaAutoGroupDestTable.setStatus(_A)
_CipslaAutoGroupDestEntry_Object=MibTableRow
cipslaAutoGroupDestEntry=_CipslaAutoGroupDestEntry_Object((1,3,6,1,4,1,9,9,633,1,2,1))
cipslaAutoGroupDestEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:cipslaAutoGroupDestEntry.setStatus(_A)
class _CipslaAutoGroupDestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaAutoGroupDestName_Type.__name__=_E
_CipslaAutoGroupDestName_Object=MibTableColumn
cipslaAutoGroupDestName=_CipslaAutoGroupDestName_Object((1,3,6,1,4,1,9,9,633,1,2,1,1),_CipslaAutoGroupDestName_Type())
cipslaAutoGroupDestName.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaAutoGroupDestName.setStatus(_A)
_CipslaAutoGroupDestIpAddrType_Type=InetAddressType
_CipslaAutoGroupDestIpAddrType_Object=MibTableColumn
cipslaAutoGroupDestIpAddrType=_CipslaAutoGroupDestIpAddrType_Object((1,3,6,1,4,1,9,9,633,1,2,1,2),_CipslaAutoGroupDestIpAddrType_Type())
cipslaAutoGroupDestIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaAutoGroupDestIpAddrType.setStatus(_A)
_CipslaAutoGroupDestIpAddr_Type=InetAddress
_CipslaAutoGroupDestIpAddr_Object=MibTableColumn
cipslaAutoGroupDestIpAddr=_CipslaAutoGroupDestIpAddr_Object((1,3,6,1,4,1,9,9,633,1,2,1,3),_CipslaAutoGroupDestIpAddr_Type())
cipslaAutoGroupDestIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaAutoGroupDestIpAddr.setStatus(_A)
_CipslaAutoGroupDestPort_Type=InetPortNumber
_CipslaAutoGroupDestPort_Object=MibTableColumn
cipslaAutoGroupDestPort=_CipslaAutoGroupDestPort_Object((1,3,6,1,4,1,9,9,633,1,2,1,4),_CipslaAutoGroupDestPort_Type())
cipslaAutoGroupDestPort.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaAutoGroupDestPort.setStatus(_A)
class _CipslaAutoGroupDestStorageType_Type(StorageType):defaultValue=3
_CipslaAutoGroupDestStorageType_Type.__name__=_H
_CipslaAutoGroupDestStorageType_Object=MibTableColumn
cipslaAutoGroupDestStorageType=_CipslaAutoGroupDestStorageType_Object((1,3,6,1,4,1,9,9,633,1,2,1,5),_CipslaAutoGroupDestStorageType_Type())
cipslaAutoGroupDestStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupDestStorageType.setStatus(_A)
_CipslaAutoGroupDestRowStatus_Type=RowStatus
_CipslaAutoGroupDestRowStatus_Object=MibTableColumn
cipslaAutoGroupDestRowStatus=_CipslaAutoGroupDestRowStatus_Object((1,3,6,1,4,1,9,9,633,1,2,1,6),_CipslaAutoGroupDestRowStatus_Type())
cipslaAutoGroupDestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupDestRowStatus.setStatus(_A)
_CipslaReactTable_Object=MibTable
cipslaReactTable=_CipslaReactTable_Object((1,3,6,1,4,1,9,9,633,1,3))
if mibBuilder.loadTexts:cipslaReactTable.setStatus(_A)
_CipslaReactEntry_Object=MibTableRow
cipslaReactEntry=_CipslaReactEntry_Object((1,3,6,1,4,1,9,9,633,1,3,1))
cipslaReactEntry.setIndexNames((0,_B,_K),(0,_B,_S),(0,_B,_L))
if mibBuilder.loadTexts:cipslaReactEntry.setStatus(_A)
class _CipslaReactConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CipslaReactConfigIndex_Type.__name__=_D
_CipslaReactConfigIndex_Object=MibTableColumn
cipslaReactConfigIndex=_CipslaReactConfigIndex_Object((1,3,6,1,4,1,9,9,633,1,3,1,1),_CipslaReactConfigIndex_Type())
cipslaReactConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaReactConfigIndex.setStatus(_A)
_CipslaReactVar_Type=IpSlaReactVar
_CipslaReactVar_Object=MibTableColumn
cipslaReactVar=_CipslaReactVar_Object((1,3,6,1,4,1,9,9,633,1,3,1,2),_CipslaReactVar_Type())
cipslaReactVar.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactVar.setStatus(_A)
class _CipslaReactThresholdType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('never',1),('immediate',2),('consecutive',3),('xOfy',4),('average',5)))
_CipslaReactThresholdType_Type.__name__=_I
_CipslaReactThresholdType_Object=MibTableColumn
cipslaReactThresholdType=_CipslaReactThresholdType_Object((1,3,6,1,4,1,9,9,633,1,3,1,3),_CipslaReactThresholdType_Type())
cipslaReactThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactThresholdType.setStatus(_A)
class _CipslaReactActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('notificationOnly',2)))
_CipslaReactActionType_Type.__name__=_I
_CipslaReactActionType_Object=MibTableColumn
cipslaReactActionType=_CipslaReactActionType_Object((1,3,6,1,4,1,9,9,633,1,3,1,4),_CipslaReactActionType_Type())
cipslaReactActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactActionType.setStatus(_A)
_CipslaReactThresholdRising_Type=Unsigned32
_CipslaReactThresholdRising_Object=MibTableColumn
cipslaReactThresholdRising=_CipslaReactThresholdRising_Object((1,3,6,1,4,1,9,9,633,1,3,1,5),_CipslaReactThresholdRising_Type())
cipslaReactThresholdRising.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactThresholdRising.setStatus(_A)
_CipslaReactThresholdFalling_Type=Unsigned32
_CipslaReactThresholdFalling_Object=MibTableColumn
cipslaReactThresholdFalling=_CipslaReactThresholdFalling_Object((1,3,6,1,4,1,9,9,633,1,3,1,6),_CipslaReactThresholdFalling_Type())
cipslaReactThresholdFalling.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactThresholdFalling.setStatus(_A)
class _CipslaReactThresholdCountX_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CipslaReactThresholdCountX_Type.__name__=_D
_CipslaReactThresholdCountX_Object=MibTableColumn
cipslaReactThresholdCountX=_CipslaReactThresholdCountX_Object((1,3,6,1,4,1,9,9,633,1,3,1,7),_CipslaReactThresholdCountX_Type())
cipslaReactThresholdCountX.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactThresholdCountX.setStatus(_A)
class _CipslaReactThresholdCountY_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CipslaReactThresholdCountY_Type.__name__=_D
_CipslaReactThresholdCountY_Object=MibTableColumn
cipslaReactThresholdCountY=_CipslaReactThresholdCountY_Object((1,3,6,1,4,1,9,9,633,1,3,1,8),_CipslaReactThresholdCountY_Type())
cipslaReactThresholdCountY.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactThresholdCountY.setStatus(_A)
class _CipslaReactStorageType_Type(StorageType):defaultValue=3
_CipslaReactStorageType_Type.__name__=_H
_CipslaReactStorageType_Object=MibTableColumn
cipslaReactStorageType=_CipslaReactStorageType_Object((1,3,6,1,4,1,9,9,633,1,3,1,9),_CipslaReactStorageType_Type())
cipslaReactStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactStorageType.setStatus(_A)
_CipslaReactRowStatus_Type=RowStatus
_CipslaReactRowStatus_Object=MibTableColumn
cipslaReactRowStatus=_CipslaReactRowStatus_Object((1,3,6,1,4,1,9,9,633,1,3,1,10),_CipslaReactRowStatus_Type())
cipslaReactRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaReactRowStatus.setStatus(_A)
_CipslaAutoGroupSchedTable_Object=MibTable
cipslaAutoGroupSchedTable=_CipslaAutoGroupSchedTable_Object((1,3,6,1,4,1,9,9,633,1,4))
if mibBuilder.loadTexts:cipslaAutoGroupSchedTable.setStatus(_A)
_CipslaAutoGroupSchedEntry_Object=MibTableRow
cipslaAutoGroupSchedEntry=_CipslaAutoGroupSchedEntry_Object((1,3,6,1,4,1,9,9,633,1,4,1))
cipslaAutoGroupSchedEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:cipslaAutoGroupSchedEntry.setStatus(_A)
class _CipslaAutoGroupSchedId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaAutoGroupSchedId_Type.__name__=_E
_CipslaAutoGroupSchedId_Object=MibTableColumn
cipslaAutoGroupSchedId=_CipslaAutoGroupSchedId_Object((1,3,6,1,4,1,9,9,633,1,4,1,1),_CipslaAutoGroupSchedId_Type())
cipslaAutoGroupSchedId.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaAutoGroupSchedId.setStatus(_A)
class _CipslaAutoGroupSchedPeriod_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,99000))
_CipslaAutoGroupSchedPeriod_Type.__name__=_D
_CipslaAutoGroupSchedPeriod_Object=MibTableColumn
cipslaAutoGroupSchedPeriod=_CipslaAutoGroupSchedPeriod_Object((1,3,6,1,4,1,9,9,633,1,4,1,2),_CipslaAutoGroupSchedPeriod_Type())
cipslaAutoGroupSchedPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedPeriod.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedPeriod.setUnits(_F)
class _CipslaAutoGroupSchedInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_CipslaAutoGroupSchedInterval_Type.__name__=_D
_CipslaAutoGroupSchedInterval_Object=MibTableColumn
cipslaAutoGroupSchedInterval=_CipslaAutoGroupSchedInterval_Object((1,3,6,1,4,1,9,9,633,1,4,1,3),_CipslaAutoGroupSchedInterval_Type())
cipslaAutoGroupSchedInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedInterval.setUnits(_F)
class _CipslaAutoGroupSchedLife_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CipslaAutoGroupSchedLife_Type.__name__=_D
_CipslaAutoGroupSchedLife_Object=MibTableColumn
cipslaAutoGroupSchedLife=_CipslaAutoGroupSchedLife_Object((1,3,6,1,4,1,9,9,633,1,4,1,4),_CipslaAutoGroupSchedLife_Type())
cipslaAutoGroupSchedLife.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedLife.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedLife.setUnits(_F)
class _CipslaAutoGroupSchedAgeout_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2073600))
_CipslaAutoGroupSchedAgeout_Type.__name__=_D
_CipslaAutoGroupSchedAgeout_Object=MibTableColumn
cipslaAutoGroupSchedAgeout=_CipslaAutoGroupSchedAgeout_Object((1,3,6,1,4,1,9,9,633,1,4,1,5),_CipslaAutoGroupSchedAgeout_Type())
cipslaAutoGroupSchedAgeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedAgeout.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedAgeout.setUnits(_F)
class _CipslaAutoGroupSchedMaxInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_CipslaAutoGroupSchedMaxInterval_Type.__name__=_D
_CipslaAutoGroupSchedMaxInterval_Object=MibTableColumn
cipslaAutoGroupSchedMaxInterval=_CipslaAutoGroupSchedMaxInterval_Object((1,3,6,1,4,1,9,9,633,1,4,1,6),_CipslaAutoGroupSchedMaxInterval_Type())
cipslaAutoGroupSchedMaxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedMaxInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedMaxInterval.setUnits(_F)
class _CipslaAutoGroupSchedMinInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_CipslaAutoGroupSchedMinInterval_Type.__name__=_D
_CipslaAutoGroupSchedMinInterval_Object=MibTableColumn
cipslaAutoGroupSchedMinInterval=_CipslaAutoGroupSchedMinInterval_Object((1,3,6,1,4,1,9,9,633,1,4,1,7),_CipslaAutoGroupSchedMinInterval_Type())
cipslaAutoGroupSchedMinInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedMinInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedMinInterval.setUnits(_F)
class _CipslaAutoGroupSchedStartTime_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_CipslaAutoGroupSchedStartTime_Type.__name__=_D
_CipslaAutoGroupSchedStartTime_Object=MibTableColumn
cipslaAutoGroupSchedStartTime=_CipslaAutoGroupSchedStartTime_Object((1,3,6,1,4,1,9,9,633,1,4,1,8),_CipslaAutoGroupSchedStartTime_Type())
cipslaAutoGroupSchedStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedStartTime.setStatus(_A)
if mibBuilder.loadTexts:cipslaAutoGroupSchedStartTime.setUnits(_F)
class _CipslaAutoGroupSchedStorageType_Type(StorageType):defaultValue=3
_CipslaAutoGroupSchedStorageType_Type.__name__=_H
_CipslaAutoGroupSchedStorageType_Object=MibTableColumn
cipslaAutoGroupSchedStorageType=_CipslaAutoGroupSchedStorageType_Object((1,3,6,1,4,1,9,9,633,1,4,1,9),_CipslaAutoGroupSchedStorageType_Type())
cipslaAutoGroupSchedStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedStorageType.setStatus(_A)
_CipslaAutoGroupSchedRowStatus_Type=RowStatus
_CipslaAutoGroupSchedRowStatus_Object=MibTableColumn
cipslaAutoGroupSchedRowStatus=_CipslaAutoGroupSchedRowStatus_Object((1,3,6,1,4,1,9,9,633,1,4,1,10),_CipslaAutoGroupSchedRowStatus_Type())
cipslaAutoGroupSchedRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaAutoGroupSchedRowStatus.setStatus(_A)
_CiscoIpSlaAutoMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpSlaAutoMIBConform=_CiscoIpSlaAutoMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,633,2))
_CiscoIpSlaAutoMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpSlaAutoMIBCompliances=_CiscoIpSlaAutoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,633,2,1))
_CiscoIpSlaAutoMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpSlaAutoMIBGroups=_CiscoIpSlaAutoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,633,2,2))
ciscoIpSlaAutoGroupConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,633,2,2,1))
ciscoIpSlaAutoGroupConfGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_L),(_B,_X),(_B,_Y),(_B,_K),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoIpSlaAutoGroupConfGroup.setStatus(_A)
ciscoIpSlaAutoGroupDestGroup=ObjectGroup((1,3,6,1,4,1,9,9,633,2,2,2))
ciscoIpSlaAutoGroupDestGroup.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoIpSlaAutoGroupDestGroup.setStatus(_A)
ciscoIpSlaAutoGroupReactGroup=ObjectGroup((1,3,6,1,4,1,9,9,633,2,2,3))
ciscoIpSlaAutoGroupReactGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoIpSlaAutoGroupReactGroup.setStatus(_A)
ciscoIpSlaAutoGroupSchedGroup=ObjectGroup((1,3,6,1,4,1,9,9,633,2,2,4))
ciscoIpSlaAutoGroupSchedGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoIpSlaAutoGroupSchedGroup.setStatus(_A)
ciscoIpSlaAutoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,633,2,1,1))
ciscoIpSlaAutoMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoIpSlaAutoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpSlaAutoMIB':ciscoIpSlaAutoMIB,'ciscoIpSlaAutoMIBNotifs':ciscoIpSlaAutoMIBNotifs,'ciscoIpSlaAutoMIBObjects':ciscoIpSlaAutoMIBObjects,'cipslaAutoGroupTable':cipslaAutoGroupTable,'cipslaAutoGroupEntry':cipslaAutoGroupEntry,_N:cipslaAutoGroupName,_U:cipslaAutoGroupDescription,_V:cipslaAutoGroupDestinationName,_W:cipslaAutoGroupADDestPort,_L:cipslaAutoGroupOperTemplateName,_X:cipslaAutoGroupSchedulerId,_Y:cipslaAutoGroupQoSEnable,_K:cipslaAutoGroupOperType,_Z:cipslaAutoGroupDestIPADEnable,_a:cipslaAutoGroupADMeasureRetry,_b:cipslaAutoGroupADDestIPAgeout,_c:cipslaAutoGroupStorageType,_d:cipslaAutoGroupRowStatus,'cipslaAutoGroupDestTable':cipslaAutoGroupDestTable,'cipslaAutoGroupDestEntry':cipslaAutoGroupDestEntry,_O:cipslaAutoGroupDestName,_P:cipslaAutoGroupDestIpAddrType,_Q:cipslaAutoGroupDestIpAddr,_R:cipslaAutoGroupDestPort,_e:cipslaAutoGroupDestStorageType,_f:cipslaAutoGroupDestRowStatus,'cipslaReactTable':cipslaReactTable,'cipslaReactEntry':cipslaReactEntry,_S:cipslaReactConfigIndex,_g:cipslaReactVar,_h:cipslaReactThresholdType,_i:cipslaReactActionType,_j:cipslaReactThresholdRising,_k:cipslaReactThresholdFalling,_l:cipslaReactThresholdCountX,_m:cipslaReactThresholdCountY,_n:cipslaReactStorageType,_o:cipslaReactRowStatus,'cipslaAutoGroupSchedTable':cipslaAutoGroupSchedTable,'cipslaAutoGroupSchedEntry':cipslaAutoGroupSchedEntry,_T:cipslaAutoGroupSchedId,_p:cipslaAutoGroupSchedPeriod,_q:cipslaAutoGroupSchedInterval,_r:cipslaAutoGroupSchedLife,_s:cipslaAutoGroupSchedAgeout,_t:cipslaAutoGroupSchedMaxInterval,_u:cipslaAutoGroupSchedMinInterval,_v:cipslaAutoGroupSchedStartTime,_w:cipslaAutoGroupSchedStorageType,_x:cipslaAutoGroupSchedRowStatus,'ciscoIpSlaAutoMIBConform':ciscoIpSlaAutoMIBConform,'ciscoIpSlaAutoMIBCompliances':ciscoIpSlaAutoMIBCompliances,'ciscoIpSlaAutoMIBCompliance':ciscoIpSlaAutoMIBCompliance,'ciscoIpSlaAutoMIBGroups':ciscoIpSlaAutoMIBGroups,_y:ciscoIpSlaAutoGroupConfGroup,_z:ciscoIpSlaAutoGroupDestGroup,_A0:ciscoIpSlaAutoGroupReactGroup,_A1:ciscoIpSlaAutoGroupSchedGroup})