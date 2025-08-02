_Q='hpnicfFCoEFIPSnoopingVLANIndex'
_P='hpnicfFCoEStaticVfcIndex'
_O='hpnicfFCoEFabricIndex'
_N='hpnicfFCoEVLANIndex'
_M='0EFC00'
_L='TruthValue'
_K='Integer32'
_J='OctetString'
_I='read-only'
_H='not-accessible'
_G='HPN-ICF-FCOE-MIB'
_F='Unsigned32'
_E='fcmInstanceIndex'
_D='FC-MGMT-MIB'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fcmInstanceIndex,=mibBuilder.importSymbols(_D,_E)
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_L)
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
hpnicfFCoE=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,120))
if mibBuilder.loadTexts:hpnicfFCoE.setRevisions(('2012-03-28 00:00',))
class HpnicfFCoEVfcBindType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('interfaceIndex',1),('macAddress',2)))
_HpnicfFCoEObjects_ObjectIdentity=ObjectIdentity
hpnicfFCoEObjects=_HpnicfFCoEObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,120,1))
_HpnicfFCoEConfig_ObjectIdentity=ObjectIdentity
hpnicfFCoEConfig=_HpnicfFCoEConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1))
_HpnicfFCoECfgTable_Object=MibTable
hpnicfFCoECfgTable=_HpnicfFCoECfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1))
if mibBuilder.loadTexts:hpnicfFCoECfgTable.setStatus(_A)
_HpnicfFCoECfgEntry_Object=MibTableRow
hpnicfFCoECfgEntry=_HpnicfFCoECfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1,1))
hpnicfFCoECfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFCoECfgEntry.setStatus(_A)
class _HpnicfFCoECfgFcmap_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfFCoECfgFcmap_Type.__name__=_J
_HpnicfFCoECfgFcmap_Object=MibTableColumn
hpnicfFCoECfgFcmap=_HpnicfFCoECfgFcmap_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1,1,1),_HpnicfFCoECfgFcmap_Type())
hpnicfFCoECfgFcmap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoECfgFcmap.setStatus(_A)
class _HpnicfFCoECfgDynamicVfcCreation_Type(TruthValue):defaultValue=2
_HpnicfFCoECfgDynamicVfcCreation_Type.__name__=_L
_HpnicfFCoECfgDynamicVfcCreation_Object=MibTableColumn
hpnicfFCoECfgDynamicVfcCreation=_HpnicfFCoECfgDynamicVfcCreation_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1,1,2),_HpnicfFCoECfgDynamicVfcCreation_Type())
hpnicfFCoECfgDynamicVfcCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoECfgDynamicVfcCreation.setStatus(_A)
class _HpnicfFCoECfgDefaultFCFPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfFCoECfgDefaultFCFPriority_Type.__name__=_F
_HpnicfFCoECfgDefaultFCFPriority_Object=MibTableColumn
hpnicfFCoECfgDefaultFCFPriority=_HpnicfFCoECfgDefaultFCFPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1,1,3),_HpnicfFCoECfgDefaultFCFPriority_Type())
hpnicfFCoECfgDefaultFCFPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoECfgDefaultFCFPriority.setStatus(_A)
class _HpnicfFCoECfgDATov_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_HpnicfFCoECfgDATov_Type.__name__=_F
_HpnicfFCoECfgDATov_Object=MibTableColumn
hpnicfFCoECfgDATov=_HpnicfFCoECfgDATov_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1,1,4),_HpnicfFCoECfgDATov_Type())
hpnicfFCoECfgDATov.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoECfgDATov.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFCoECfgDATov.setUnits('seconds')
class _HpnicfFCoECfgAddressingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fpma',1),('spma',2),('fpmaAndSpma',3)))
_HpnicfFCoECfgAddressingMode_Type.__name__=_K
_HpnicfFCoECfgAddressingMode_Object=MibTableColumn
hpnicfFCoECfgAddressingMode=_HpnicfFCoECfgAddressingMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,1,1,5),_HpnicfFCoECfgAddressingMode_Type())
hpnicfFCoECfgAddressingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoECfgAddressingMode.setStatus(_A)
_HpnicfFCoEVLANTable_Object=MibTable
hpnicfFCoEVLANTable=_HpnicfFCoEVLANTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,2))
if mibBuilder.loadTexts:hpnicfFCoEVLANTable.setStatus(_A)
_HpnicfFCoEVLANEntry_Object=MibTableRow
hpnicfFCoEVLANEntry=_HpnicfFCoEVLANEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,2,1))
hpnicfFCoEVLANEntry.setIndexNames((0,_D,_E),(0,_G,_N),(0,_G,_O))
if mibBuilder.loadTexts:hpnicfFCoEVLANEntry.setStatus(_A)
_HpnicfFCoEVLANIndex_Type=VlanIndex
_HpnicfFCoEVLANIndex_Object=MibTableColumn
hpnicfFCoEVLANIndex=_HpnicfFCoEVLANIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,2,1,1),_HpnicfFCoEVLANIndex_Type())
hpnicfFCoEVLANIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFCoEVLANIndex.setStatus(_A)
_HpnicfFCoEFabricIndex_Type=T11FabricIndex
_HpnicfFCoEFabricIndex_Object=MibTableColumn
hpnicfFCoEFabricIndex=_HpnicfFCoEFabricIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,2,1,2),_HpnicfFCoEFabricIndex_Type())
hpnicfFCoEFabricIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFCoEFabricIndex.setStatus(_A)
class _HpnicfFCoEVLANOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpnicfFCoEVLANOperState_Type.__name__=_K
_HpnicfFCoEVLANOperState_Object=MibTableColumn
hpnicfFCoEVLANOperState=_HpnicfFCoEVLANOperState_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,2,1,3),_HpnicfFCoEVLANOperState_Type())
hpnicfFCoEVLANOperState.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFCoEVLANOperState.setStatus(_A)
_HpnicfFCoEVLANRowStatus_Type=RowStatus
_HpnicfFCoEVLANRowStatus_Object=MibTableColumn
hpnicfFCoEVLANRowStatus=_HpnicfFCoEVLANRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,2,1,4),_HpnicfFCoEVLANRowStatus_Type())
hpnicfFCoEVLANRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFCoEVLANRowStatus.setStatus(_A)
_HpnicfFCoEStaticVfcTable_Object=MibTable
hpnicfFCoEStaticVfcTable=_HpnicfFCoEStaticVfcTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3))
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcTable.setStatus(_A)
_HpnicfFCoEStaticVfcEntry_Object=MibTableRow
hpnicfFCoEStaticVfcEntry=_HpnicfFCoEStaticVfcEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1))
hpnicfFCoEStaticVfcEntry.setIndexNames((0,_D,_E),(0,_G,_P))
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcEntry.setStatus(_A)
class _HpnicfFCoEStaticVfcIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfFCoEStaticVfcIndex_Type.__name__=_F
_HpnicfFCoEStaticVfcIndex_Object=MibTableColumn
hpnicfFCoEStaticVfcIndex=_HpnicfFCoEStaticVfcIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,1),_HpnicfFCoEStaticVfcIndex_Type())
hpnicfFCoEStaticVfcIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcIndex.setStatus(_A)
class _HpnicfFCoEStaticVfcFCFPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfFCoEStaticVfcFCFPriority_Type.__name__=_F
_HpnicfFCoEStaticVfcFCFPriority_Object=MibTableColumn
hpnicfFCoEStaticVfcFCFPriority=_HpnicfFCoEStaticVfcFCFPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,2),_HpnicfFCoEStaticVfcFCFPriority_Type())
hpnicfFCoEStaticVfcFCFPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcFCFPriority.setStatus(_A)
_HpnicfFCoEStaticVfcBindType_Type=HpnicfFCoEVfcBindType
_HpnicfFCoEStaticVfcBindType_Object=MibTableColumn
hpnicfFCoEStaticVfcBindType=_HpnicfFCoEStaticVfcBindType_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,3),_HpnicfFCoEStaticVfcBindType_Type())
hpnicfFCoEStaticVfcBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcBindType.setStatus(_A)
_HpnicfFCoEStaticVfcBindIfIndex_Type=InterfaceIndexOrZero
_HpnicfFCoEStaticVfcBindIfIndex_Object=MibTableColumn
hpnicfFCoEStaticVfcBindIfIndex=_HpnicfFCoEStaticVfcBindIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,4),_HpnicfFCoEStaticVfcBindIfIndex_Type())
hpnicfFCoEStaticVfcBindIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcBindIfIndex.setStatus(_A)
_HpnicfFCoEStaticVfcBindMACAddress_Type=MacAddress
_HpnicfFCoEStaticVfcBindMACAddress_Object=MibTableColumn
hpnicfFCoEStaticVfcBindMACAddress=_HpnicfFCoEStaticVfcBindMACAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,5),_HpnicfFCoEStaticVfcBindMACAddress_Type())
hpnicfFCoEStaticVfcBindMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcBindMACAddress.setStatus(_A)
_HpnicfFCoEStaticVfcIfIndex_Type=InterfaceIndex
_HpnicfFCoEStaticVfcIfIndex_Object=MibTableColumn
hpnicfFCoEStaticVfcIfIndex=_HpnicfFCoEStaticVfcIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,6),_HpnicfFCoEStaticVfcIfIndex_Type())
hpnicfFCoEStaticVfcIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcIfIndex.setStatus(_A)
_HpnicfFCoEStaticVfcCreationTime_Type=TimeStamp
_HpnicfFCoEStaticVfcCreationTime_Object=MibTableColumn
hpnicfFCoEStaticVfcCreationTime=_HpnicfFCoEStaticVfcCreationTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,7),_HpnicfFCoEStaticVfcCreationTime_Type())
hpnicfFCoEStaticVfcCreationTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcCreationTime.setStatus(_A)
_HpnicfFCoEStaticVfcFailureCause_Type=SnmpAdminString
_HpnicfFCoEStaticVfcFailureCause_Object=MibTableColumn
hpnicfFCoEStaticVfcFailureCause=_HpnicfFCoEStaticVfcFailureCause_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,8),_HpnicfFCoEStaticVfcFailureCause_Type())
hpnicfFCoEStaticVfcFailureCause.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcFailureCause.setStatus(_A)
_HpnicfFCoEStaticVfcRowStatus_Type=RowStatus
_HpnicfFCoEStaticVfcRowStatus_Object=MibTableColumn
hpnicfFCoEStaticVfcRowStatus=_HpnicfFCoEStaticVfcRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,3,1,9),_HpnicfFCoEStaticVfcRowStatus_Type())
hpnicfFCoEStaticVfcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFCoEStaticVfcRowStatus.setStatus(_A)
_HpnicfFCoEFIPSnoopingTable_Object=MibTable
hpnicfFCoEFIPSnoopingTable=_HpnicfFCoEFIPSnoopingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,4))
if mibBuilder.loadTexts:hpnicfFCoEFIPSnoopingTable.setStatus(_A)
_HpnicfFCoEFIPSnoopingEntry_Object=MibTableRow
hpnicfFCoEFIPSnoopingEntry=_HpnicfFCoEFIPSnoopingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,4,1))
hpnicfFCoEFIPSnoopingEntry.setIndexNames((0,_D,_E),(0,_G,_Q))
if mibBuilder.loadTexts:hpnicfFCoEFIPSnoopingEntry.setStatus(_A)
_HpnicfFCoEFIPSnoopingVLANIndex_Type=VlanIndex
_HpnicfFCoEFIPSnoopingVLANIndex_Object=MibTableColumn
hpnicfFCoEFIPSnoopingVLANIndex=_HpnicfFCoEFIPSnoopingVLANIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,4,1,1),_HpnicfFCoEFIPSnoopingVLANIndex_Type())
hpnicfFCoEFIPSnoopingVLANIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFCoEFIPSnoopingVLANIndex.setStatus(_A)
class _HpnicfFCoEFIPSnoopingEnable_Type(TruthValue):defaultValue=2
_HpnicfFCoEFIPSnoopingEnable_Type.__name__=_L
_HpnicfFCoEFIPSnoopingEnable_Object=MibTableColumn
hpnicfFCoEFIPSnoopingEnable=_HpnicfFCoEFIPSnoopingEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,4,1,2),_HpnicfFCoEFIPSnoopingEnable_Type())
hpnicfFCoEFIPSnoopingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoEFIPSnoopingEnable.setStatus(_A)
class _HpnicfFCoEFIPSnoopingFcmap_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfFCoEFIPSnoopingFcmap_Type.__name__=_J
_HpnicfFCoEFIPSnoopingFcmap_Object=MibTableColumn
hpnicfFCoEFIPSnoopingFcmap=_HpnicfFCoEFIPSnoopingFcmap_Object((1,3,6,1,4,1,11,2,14,11,15,2,120,1,1,4,1,3),_HpnicfFCoEFIPSnoopingFcmap_Type())
hpnicfFCoEFIPSnoopingFcmap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFCoEFIPSnoopingFcmap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'HpnicfFCoEVfcBindType':HpnicfFCoEVfcBindType,'hpnicfFCoE':hpnicfFCoE,'hpnicfFCoEObjects':hpnicfFCoEObjects,'hpnicfFCoEConfig':hpnicfFCoEConfig,'hpnicfFCoECfgTable':hpnicfFCoECfgTable,'hpnicfFCoECfgEntry':hpnicfFCoECfgEntry,'hpnicfFCoECfgFcmap':hpnicfFCoECfgFcmap,'hpnicfFCoECfgDynamicVfcCreation':hpnicfFCoECfgDynamicVfcCreation,'hpnicfFCoECfgDefaultFCFPriority':hpnicfFCoECfgDefaultFCFPriority,'hpnicfFCoECfgDATov':hpnicfFCoECfgDATov,'hpnicfFCoECfgAddressingMode':hpnicfFCoECfgAddressingMode,'hpnicfFCoEVLANTable':hpnicfFCoEVLANTable,'hpnicfFCoEVLANEntry':hpnicfFCoEVLANEntry,_N:hpnicfFCoEVLANIndex,_O:hpnicfFCoEFabricIndex,'hpnicfFCoEVLANOperState':hpnicfFCoEVLANOperState,'hpnicfFCoEVLANRowStatus':hpnicfFCoEVLANRowStatus,'hpnicfFCoEStaticVfcTable':hpnicfFCoEStaticVfcTable,'hpnicfFCoEStaticVfcEntry':hpnicfFCoEStaticVfcEntry,_P:hpnicfFCoEStaticVfcIndex,'hpnicfFCoEStaticVfcFCFPriority':hpnicfFCoEStaticVfcFCFPriority,'hpnicfFCoEStaticVfcBindType':hpnicfFCoEStaticVfcBindType,'hpnicfFCoEStaticVfcBindIfIndex':hpnicfFCoEStaticVfcBindIfIndex,'hpnicfFCoEStaticVfcBindMACAddress':hpnicfFCoEStaticVfcBindMACAddress,'hpnicfFCoEStaticVfcIfIndex':hpnicfFCoEStaticVfcIfIndex,'hpnicfFCoEStaticVfcCreationTime':hpnicfFCoEStaticVfcCreationTime,'hpnicfFCoEStaticVfcFailureCause':hpnicfFCoEStaticVfcFailureCause,'hpnicfFCoEStaticVfcRowStatus':hpnicfFCoEStaticVfcRowStatus,'hpnicfFCoEFIPSnoopingTable':hpnicfFCoEFIPSnoopingTable,'hpnicfFCoEFIPSnoopingEntry':hpnicfFCoEFIPSnoopingEntry,_Q:hpnicfFCoEFIPSnoopingVLANIndex,'hpnicfFCoEFIPSnoopingEnable':hpnicfFCoEFIPSnoopingEnable,'hpnicfFCoEFIPSnoopingFcmap':hpnicfFCoEFIPSnoopingFcmap})