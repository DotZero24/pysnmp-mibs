_W='enabled'
_V='disabled'
_U='hpnicfEvbVSIVlanId'
_T='hpnicfEvbVSIMac'
_S='hpnicfEvbGroupID'
_R='hpnicfEvbManagerIndex'
_Q='hpnicfEvbVSILocalID'
_P='hpnicfEvbSBPPortNumber'
_O='hpnicfEvbPortNumber'
_N='unknown'
_M='OctetString'
_L='hpnicfFlex10PortNumber'
_K='hpnicfEvbSchannelID'
_J='Bits'
_I='TruthValue'
_H='Unsigned32'
_G='read-write'
_F='Integer32'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='HPN-ICF-EVB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
IEEE8021BridgePortNumber,=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021BridgePortNumber')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
hpnicfEvb=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,134))
if mibBuilder.loadTexts:hpnicfEvb.setRevisions(('2012-12-21 12:00',))
_HpnicfEvbSysObjects_ObjectIdentity=ObjectIdentity
hpnicfEvbSysObjects=_HpnicfEvbSysObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,134,1))
class _HpnicfEvbSetResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('processing',2),('success',3),('failed',4)))
_HpnicfEvbSetResult_Type.__name__=_F
_HpnicfEvbSetResult_Object=MibScalar
hpnicfEvbSetResult=_HpnicfEvbSetResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,1),_HpnicfEvbSetResult_Type())
hpnicfEvbSetResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvbSetResult.setStatus(_A)
_HpnicfEvbDefaultManagerTable_Object=MibTable
hpnicfEvbDefaultManagerTable=_HpnicfEvbDefaultManagerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2))
if mibBuilder.loadTexts:hpnicfEvbDefaultManagerTable.setStatus(_A)
_HpnicfEvbDefaultManagerEntry_Object=MibTableRow
hpnicfEvbDefaultManagerEntry=_HpnicfEvbDefaultManagerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2,1))
hpnicfEvbDefaultManagerEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hpnicfEvbDefaultManagerEntry.setStatus(_A)
_HpnicfEvbManagerIndex_Type=Unsigned32
_HpnicfEvbManagerIndex_Object=MibTableColumn
hpnicfEvbManagerIndex=_HpnicfEvbManagerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2,1,1),_HpnicfEvbManagerIndex_Type())
hpnicfEvbManagerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbManagerIndex.setStatus(_A)
class _HpnicfEvbManagerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('name',3),('local',4)))
_HpnicfEvbManagerType_Type.__name__=_F
_HpnicfEvbManagerType_Object=MibTableColumn
hpnicfEvbManagerType=_HpnicfEvbManagerType_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2,1,2),_HpnicfEvbManagerType_Type())
hpnicfEvbManagerType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbManagerType.setStatus(_A)
class _HpnicfEvbManagerID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfEvbManagerID_Type.__name__=_M
_HpnicfEvbManagerID_Object=MibTableColumn
hpnicfEvbManagerID=_HpnicfEvbManagerID_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2,1,3),_HpnicfEvbManagerID_Type())
hpnicfEvbManagerID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbManagerID.setStatus(_A)
class _HpnicfEvbManagerPort_Type(Unsigned32):defaultValue=8080;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfEvbManagerPort_Type.__name__=_H
_HpnicfEvbManagerPort_Object=MibTableColumn
hpnicfEvbManagerPort=_HpnicfEvbManagerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2,1,4),_HpnicfEvbManagerPort_Type())
hpnicfEvbManagerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbManagerPort.setStatus(_A)
_HpnicfEvbManagerRowStatus_Type=RowStatus
_HpnicfEvbManagerRowStatus_Object=MibTableColumn
hpnicfEvbManagerRowStatus=_HpnicfEvbManagerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,1,2,1,5),_HpnicfEvbManagerRowStatus_Type())
hpnicfEvbManagerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbManagerRowStatus.setStatus(_A)
_HpnicfEvbPortObjects_ObjectIdentity=ObjectIdentity
hpnicfEvbPortObjects=_HpnicfEvbPortObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,134,2))
_HpnicfEvbPortConfigTable_Object=MibTable
hpnicfEvbPortConfigTable=_HpnicfEvbPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,1))
if mibBuilder.loadTexts:hpnicfEvbPortConfigTable.setStatus(_A)
_HpnicfEvbPortConfigEntry_Object=MibTableRow
hpnicfEvbPortConfigEntry=_HpnicfEvbPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,1,1))
hpnicfEvbPortConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:hpnicfEvbPortConfigEntry.setStatus(_A)
_HpnicfEvbPortNumber_Type=IEEE8021BridgePortNumber
_HpnicfEvbPortNumber_Object=MibTableColumn
hpnicfEvbPortNumber=_HpnicfEvbPortNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,1,1,1),_HpnicfEvbPortNumber_Type())
hpnicfEvbPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbPortNumber.setStatus(_A)
class _HpnicfEvbRWD_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,31))
_HpnicfEvbRWD_Type.__name__=_H
_HpnicfEvbRWD_Object=MibTableColumn
hpnicfEvbRWD=_HpnicfEvbRWD_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,1,1,2),_HpnicfEvbRWD_Type())
hpnicfEvbRWD.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEvbRWD.setStatus(_A)
class _HpnicfEvbRKA_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(14,31))
_HpnicfEvbRKA_Type.__name__=_H
_HpnicfEvbRKA_Object=MibTableColumn
hpnicfEvbRKA=_HpnicfEvbRKA_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,1,1,3),_HpnicfEvbRKA_Type())
hpnicfEvbRKA.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEvbRKA.setStatus(_A)
_HpnicfEvbSchannelConfigTable_Object=MibTable
hpnicfEvbSchannelConfigTable=_HpnicfEvbSchannelConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2))
if mibBuilder.loadTexts:hpnicfEvbSchannelConfigTable.setStatus(_A)
_HpnicfEvbSchannelConfigEntry_Object=MibTableRow
hpnicfEvbSchannelConfigEntry=_HpnicfEvbSchannelConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2,1))
hpnicfEvbSchannelConfigEntry.setIndexNames((0,_B,_O),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfEvbSchannelConfigEntry.setStatus(_A)
_HpnicfEvbSchannelID_Type=Unsigned32
_HpnicfEvbSchannelID_Object=MibTableColumn
hpnicfEvbSchannelID=_HpnicfEvbSchannelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2,1,1),_HpnicfEvbSchannelID_Type())
hpnicfEvbSchannelID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbSchannelID.setStatus(_A)
class _HpnicfEvbSchannelSVLAN_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfEvbSchannelSVLAN_Type.__name__=_H
_HpnicfEvbSchannelSVLAN_Object=MibTableColumn
hpnicfEvbSchannelSVLAN=_HpnicfEvbSchannelSVLAN_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2,1,2),_HpnicfEvbSchannelSVLAN_Type())
hpnicfEvbSchannelSVLAN.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbSchannelSVLAN.setStatus(_A)
class _HpnicfEvbMacLearningStatus_Type(TruthValue):defaultValue=1
_HpnicfEvbMacLearningStatus_Type.__name__=_I
_HpnicfEvbMacLearningStatus_Object=MibTableColumn
hpnicfEvbMacLearningStatus=_HpnicfEvbMacLearningStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2,1,3),_HpnicfEvbMacLearningStatus_Type())
hpnicfEvbMacLearningStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEvbMacLearningStatus.setStatus(_A)
class _HpnicfEvbRRStatus_Type(TruthValue):defaultValue=2
_HpnicfEvbRRStatus_Type.__name__=_I
_HpnicfEvbRRStatus_Object=MibTableColumn
hpnicfEvbRRStatus=_HpnicfEvbRRStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2,1,4),_HpnicfEvbRRStatus_Type())
hpnicfEvbRRStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEvbRRStatus.setStatus(_A)
_HpnicfEvbSchannelRowStatus_Type=RowStatus
_HpnicfEvbSchannelRowStatus_Object=MibTableColumn
hpnicfEvbSchannelRowStatus=_HpnicfEvbSchannelRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,2,1,5),_HpnicfEvbSchannelRowStatus_Type())
hpnicfEvbSchannelRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbSchannelRowStatus.setStatus(_A)
_HpnicfEvbVSIConfigTable_Object=MibTable
hpnicfEvbVSIConfigTable=_HpnicfEvbVSIConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3))
if mibBuilder.loadTexts:hpnicfEvbVSIConfigTable.setStatus(_A)
_HpnicfEvbVSIConfigEntry_Object=MibTableRow
hpnicfEvbVSIConfigEntry=_HpnicfEvbVSIConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1))
hpnicfEvbVSIConfigEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfEvbVSIConfigEntry.setStatus(_A)
_HpnicfEvbSBPPortNumber_Type=IEEE8021BridgePortNumber
_HpnicfEvbSBPPortNumber_Object=MibTableColumn
hpnicfEvbSBPPortNumber=_HpnicfEvbSBPPortNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1,1),_HpnicfEvbSBPPortNumber_Type())
hpnicfEvbSBPPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbSBPPortNumber.setStatus(_A)
_HpnicfEvbVSILocalID_Type=Unsigned32
_HpnicfEvbVSILocalID_Object=MibTableColumn
hpnicfEvbVSILocalID=_HpnicfEvbVSILocalID_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1,2),_HpnicfEvbVSILocalID_Type())
hpnicfEvbVSILocalID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbVSILocalID.setStatus(_A)
class _HpnicfEvbVSICommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('preAssociate',1),('preAssociateWithRsrcReservation',2),('associate',3),('deAssociate',4)))
_HpnicfEvbVSICommand_Type.__name__=_F
_HpnicfEvbVSICommand_Object=MibTableColumn
hpnicfEvbVSICommand=_HpnicfEvbVSICommand_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1,3),_HpnicfEvbVSICommand_Type())
hpnicfEvbVSICommand.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbVSICommand.setStatus(_A)
_HpnicfEvbVSIIfIndex_Type=InterfaceIndexOrZero
_HpnicfEvbVSIIfIndex_Object=MibTableColumn
hpnicfEvbVSIIfIndex=_HpnicfEvbVSIIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1,4),_HpnicfEvbVSIIfIndex_Type())
hpnicfEvbVSIIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvbVSIIfIndex.setStatus(_A)
class _HpnicfEvbVSIIsActive_Type(TruthValue):defaultValue=2
_HpnicfEvbVSIIsActive_Type.__name__=_I
_HpnicfEvbVSIIsActive_Object=MibTableColumn
hpnicfEvbVSIIsActive=_HpnicfEvbVSIIsActive_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1,5),_HpnicfEvbVSIIsActive_Type())
hpnicfEvbVSIIsActive.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEvbVSIIsActive.setStatus(_A)
_HpnicfEvbVSIRowStatus_Type=RowStatus
_HpnicfEvbVSIRowStatus_Object=MibTableColumn
hpnicfEvbVSIRowStatus=_HpnicfEvbVSIRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,3,1,6),_HpnicfEvbVSIRowStatus_Type())
hpnicfEvbVSIRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbVSIRowStatus.setStatus(_A)
_HpnicfEvbVSIFilterConfigTable_Object=MibTable
hpnicfEvbVSIFilterConfigTable=_HpnicfEvbVSIFilterConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,4))
if mibBuilder.loadTexts:hpnicfEvbVSIFilterConfigTable.setStatus(_A)
_HpnicfEvbVSIFilterConfigEntry_Object=MibTableRow
hpnicfEvbVSIFilterConfigEntry=_HpnicfEvbVSIFilterConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,4,1))
hpnicfEvbVSIFilterConfigEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:hpnicfEvbVSIFilterConfigEntry.setStatus(_A)
_HpnicfEvbGroupID_Type=Unsigned32
_HpnicfEvbGroupID_Object=MibTableColumn
hpnicfEvbGroupID=_HpnicfEvbGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,4,1,1),_HpnicfEvbGroupID_Type())
hpnicfEvbGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbGroupID.setStatus(_A)
_HpnicfEvbVSIMac_Type=MacAddress
_HpnicfEvbVSIMac_Object=MibTableColumn
hpnicfEvbVSIMac=_HpnicfEvbVSIMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,4,1,2),_HpnicfEvbVSIMac_Type())
hpnicfEvbVSIMac.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbVSIMac.setStatus(_A)
_HpnicfEvbVSIVlanId_Type=VlanIndex
_HpnicfEvbVSIVlanId_Object=MibTableColumn
hpnicfEvbVSIVlanId=_HpnicfEvbVSIVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,4,1,3),_HpnicfEvbVSIVlanId_Type())
hpnicfEvbVSIVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEvbVSIVlanId.setStatus(_A)
_HpnicfEvbVSIFilterRowStatus_Type=RowStatus
_HpnicfEvbVSIFilterRowStatus_Object=MibTableColumn
hpnicfEvbVSIFilterRowStatus=_HpnicfEvbVSIFilterRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,2,4,1,4),_HpnicfEvbVSIFilterRowStatus_Type())
hpnicfEvbVSIFilterRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEvbVSIFilterRowStatus.setStatus(_A)
_HpnicfFlex10Objects_ObjectIdentity=ObjectIdentity
hpnicfFlex10Objects=_HpnicfFlex10Objects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,134,3))
_HpnicfFlex10PortConfigTable_Object=MibTable
hpnicfFlex10PortConfigTable=_HpnicfFlex10PortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,1))
if mibBuilder.loadTexts:hpnicfFlex10PortConfigTable.setStatus(_A)
_HpnicfFlex10PortConfigEntry_Object=MibTableRow
hpnicfFlex10PortConfigEntry=_HpnicfFlex10PortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,1,1))
hpnicfFlex10PortConfigEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:hpnicfFlex10PortConfigEntry.setStatus(_A)
_HpnicfFlex10PortNumber_Type=IEEE8021BridgePortNumber
_HpnicfFlex10PortNumber_Object=MibTableColumn
hpnicfFlex10PortNumber=_HpnicfFlex10PortNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,1,1,1),_HpnicfFlex10PortNumber_Type())
hpnicfFlex10PortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFlex10PortNumber.setStatus(_A)
class _HpnicfFlex10PortEnableStatus_Type(TruthValue):defaultValue=2
_HpnicfFlex10PortEnableStatus_Type.__name__=_I
_HpnicfFlex10PortEnableStatus_Object=MibTableColumn
hpnicfFlex10PortEnableStatus=_HpnicfFlex10PortEnableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,1,1,2),_HpnicfFlex10PortEnableStatus_Type())
hpnicfFlex10PortEnableStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFlex10PortEnableStatus.setStatus(_A)
_HpnicfFlex10RemoteSchannelTable_Object=MibTable
hpnicfFlex10RemoteSchannelTable=_HpnicfFlex10RemoteSchannelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2))
if mibBuilder.loadTexts:hpnicfFlex10RemoteSchannelTable.setStatus(_A)
_HpnicfFlex10RemoteSchannelEntry_Object=MibTableRow
hpnicfFlex10RemoteSchannelEntry=_HpnicfFlex10RemoteSchannelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1))
hpnicfFlex10RemoteSchannelEntry.setIndexNames((0,_B,_L),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfFlex10RemoteSchannelEntry.setStatus(_A)
class _HpnicfFlex10RemSchDesFormat_Type(Bits):namedValues=NamedValues(*(('format0',0),('format1',1)))
_HpnicfFlex10RemSchDesFormat_Type.__name__=_J
_HpnicfFlex10RemSchDesFormat_Object=MibTableColumn
hpnicfFlex10RemSchDesFormat=_HpnicfFlex10RemSchDesFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,1),_HpnicfFlex10RemSchDesFormat_Type())
hpnicfFlex10RemSchDesFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchDesFormat.setStatus(_A)
_HpnicfFlex10RemSchTerminationType_Type=Integer32
_HpnicfFlex10RemSchTerminationType_Object=MibTableColumn
hpnicfFlex10RemSchTerminationType=_HpnicfFlex10RemSchTerminationType_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,2),_HpnicfFlex10RemSchTerminationType_Type())
hpnicfFlex10RemSchTerminationType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchTerminationType.setStatus(_A)
class _HpnicfFlex10RemSchTerminationCap_Type(Bits):namedValues=NamedValues(*(('ethernet',0),('fCOE',1),('iSCSI',2),('roCEE',3)))
_HpnicfFlex10RemSchTerminationCap_Type.__name__=_J
_HpnicfFlex10RemSchTerminationCap_Object=MibTableColumn
hpnicfFlex10RemSchTerminationCap=_HpnicfFlex10RemSchTerminationCap_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,3),_HpnicfFlex10RemSchTerminationCap_Type())
hpnicfFlex10RemSchTerminationCap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchTerminationCap.setStatus(_A)
class _HpnicfFlex10RemSchTrafficClass_Type(Bits):namedValues=NamedValues(*(('class0',0),('class1',1),('class2',2),('class3',3),('class4',4),('class5',5),('class6',6),('class7',7)))
_HpnicfFlex10RemSchTrafficClass_Type.__name__=_J
_HpnicfFlex10RemSchTrafficClass_Object=MibTableColumn
hpnicfFlex10RemSchTrafficClass=_HpnicfFlex10RemSchTrafficClass_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,4),_HpnicfFlex10RemSchTrafficClass_Type())
hpnicfFlex10RemSchTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchTrafficClass.setStatus(_A)
_HpnicfFlex10RemSchCir_Type=Integer32
_HpnicfFlex10RemSchCir_Object=MibTableColumn
hpnicfFlex10RemSchCir=_HpnicfFlex10RemSchCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,5),_HpnicfFlex10RemSchCir_Type())
hpnicfFlex10RemSchCir.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchCir.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlex10RemSchCir.setUnits('mbps')
_HpnicfFlex10RemSchPir_Type=Integer32
_HpnicfFlex10RemSchPir_Object=MibTableColumn
hpnicfFlex10RemSchPir=_HpnicfFlex10RemSchPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,6),_HpnicfFlex10RemSchPir_Type())
hpnicfFlex10RemSchPir.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchPir.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlex10RemSchPir.setUnits('mbps')
class _HpnicfFlex10RemSchConnectionID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpnicfFlex10RemSchConnectionID_Type.__name__=_M
_HpnicfFlex10RemSchConnectionID_Object=MibTableColumn
hpnicfFlex10RemSchConnectionID=_HpnicfFlex10RemSchConnectionID_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,2,1,7),_HpnicfFlex10RemSchConnectionID_Type())
hpnicfFlex10RemSchConnectionID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10RemSchConnectionID.setStatus(_A)
_HpnicfFlex10SchannelLinkCtlTable_Object=MibTable
hpnicfFlex10SchannelLinkCtlTable=_HpnicfFlex10SchannelLinkCtlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,3))
if mibBuilder.loadTexts:hpnicfFlex10SchannelLinkCtlTable.setStatus(_A)
_HpnicfFlex10SchannelLinkCtlEntry_Object=MibTableRow
hpnicfFlex10SchannelLinkCtlEntry=_HpnicfFlex10SchannelLinkCtlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,3,1))
hpnicfFlex10SchannelLinkCtlEntry.setIndexNames((0,_B,_L),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfFlex10SchannelLinkCtlEntry.setStatus(_A)
_HpnicfFlex10SchannelSVID_Type=VlanIndex
_HpnicfFlex10SchannelSVID_Object=MibTableColumn
hpnicfFlex10SchannelSVID=_HpnicfFlex10SchannelSVID_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,3,1,1),_HpnicfFlex10SchannelSVID_Type())
hpnicfFlex10SchannelSVID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10SchannelSVID.setStatus(_A)
class _HpnicfFlex10SchannelLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_V,2),(_W,3)))
_HpnicfFlex10SchannelLocalStatus_Type.__name__=_F
_HpnicfFlex10SchannelLocalStatus_Object=MibTableColumn
hpnicfFlex10SchannelLocalStatus=_HpnicfFlex10SchannelLocalStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,3,1,2),_HpnicfFlex10SchannelLocalStatus_Type())
hpnicfFlex10SchannelLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10SchannelLocalStatus.setStatus(_A)
class _HpnicfFlex10SchannelRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_V,2),(_W,3)))
_HpnicfFlex10SchannelRemoteStatus_Type.__name__=_F
_HpnicfFlex10SchannelRemoteStatus_Object=MibTableColumn
hpnicfFlex10SchannelRemoteStatus=_HpnicfFlex10SchannelRemoteStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,134,3,3,1,3),_HpnicfFlex10SchannelRemoteStatus_Type())
hpnicfFlex10SchannelRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlex10SchannelRemoteStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfEvb':hpnicfEvb,'hpnicfEvbSysObjects':hpnicfEvbSysObjects,'hpnicfEvbSetResult':hpnicfEvbSetResult,'hpnicfEvbDefaultManagerTable':hpnicfEvbDefaultManagerTable,'hpnicfEvbDefaultManagerEntry':hpnicfEvbDefaultManagerEntry,_R:hpnicfEvbManagerIndex,'hpnicfEvbManagerType':hpnicfEvbManagerType,'hpnicfEvbManagerID':hpnicfEvbManagerID,'hpnicfEvbManagerPort':hpnicfEvbManagerPort,'hpnicfEvbManagerRowStatus':hpnicfEvbManagerRowStatus,'hpnicfEvbPortObjects':hpnicfEvbPortObjects,'hpnicfEvbPortConfigTable':hpnicfEvbPortConfigTable,'hpnicfEvbPortConfigEntry':hpnicfEvbPortConfigEntry,_O:hpnicfEvbPortNumber,'hpnicfEvbRWD':hpnicfEvbRWD,'hpnicfEvbRKA':hpnicfEvbRKA,'hpnicfEvbSchannelConfigTable':hpnicfEvbSchannelConfigTable,'hpnicfEvbSchannelConfigEntry':hpnicfEvbSchannelConfigEntry,_K:hpnicfEvbSchannelID,'hpnicfEvbSchannelSVLAN':hpnicfEvbSchannelSVLAN,'hpnicfEvbMacLearningStatus':hpnicfEvbMacLearningStatus,'hpnicfEvbRRStatus':hpnicfEvbRRStatus,'hpnicfEvbSchannelRowStatus':hpnicfEvbSchannelRowStatus,'hpnicfEvbVSIConfigTable':hpnicfEvbVSIConfigTable,'hpnicfEvbVSIConfigEntry':hpnicfEvbVSIConfigEntry,_P:hpnicfEvbSBPPortNumber,_Q:hpnicfEvbVSILocalID,'hpnicfEvbVSICommand':hpnicfEvbVSICommand,'hpnicfEvbVSIIfIndex':hpnicfEvbVSIIfIndex,'hpnicfEvbVSIIsActive':hpnicfEvbVSIIsActive,'hpnicfEvbVSIRowStatus':hpnicfEvbVSIRowStatus,'hpnicfEvbVSIFilterConfigTable':hpnicfEvbVSIFilterConfigTable,'hpnicfEvbVSIFilterConfigEntry':hpnicfEvbVSIFilterConfigEntry,_S:hpnicfEvbGroupID,_T:hpnicfEvbVSIMac,_U:hpnicfEvbVSIVlanId,'hpnicfEvbVSIFilterRowStatus':hpnicfEvbVSIFilterRowStatus,'hpnicfFlex10Objects':hpnicfFlex10Objects,'hpnicfFlex10PortConfigTable':hpnicfFlex10PortConfigTable,'hpnicfFlex10PortConfigEntry':hpnicfFlex10PortConfigEntry,_L:hpnicfFlex10PortNumber,'hpnicfFlex10PortEnableStatus':hpnicfFlex10PortEnableStatus,'hpnicfFlex10RemoteSchannelTable':hpnicfFlex10RemoteSchannelTable,'hpnicfFlex10RemoteSchannelEntry':hpnicfFlex10RemoteSchannelEntry,'hpnicfFlex10RemSchDesFormat':hpnicfFlex10RemSchDesFormat,'hpnicfFlex10RemSchTerminationType':hpnicfFlex10RemSchTerminationType,'hpnicfFlex10RemSchTerminationCap':hpnicfFlex10RemSchTerminationCap,'hpnicfFlex10RemSchTrafficClass':hpnicfFlex10RemSchTrafficClass,'hpnicfFlex10RemSchCir':hpnicfFlex10RemSchCir,'hpnicfFlex10RemSchPir':hpnicfFlex10RemSchPir,'hpnicfFlex10RemSchConnectionID':hpnicfFlex10RemSchConnectionID,'hpnicfFlex10SchannelLinkCtlTable':hpnicfFlex10SchannelLinkCtlTable,'hpnicfFlex10SchannelLinkCtlEntry':hpnicfFlex10SchannelLinkCtlEntry,'hpnicfFlex10SchannelSVID':hpnicfFlex10SchannelSVID,'hpnicfFlex10SchannelLocalStatus':hpnicfFlex10SchannelLocalStatus,'hpnicfFlex10SchannelRemoteStatus':hpnicfFlex10SchannelRemoteStatus})