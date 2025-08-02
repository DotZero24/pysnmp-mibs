_O='h3cFCoEStaticVfcIndex'
_N='h3cFCoEFabricIndex'
_M='h3cFCoEVLANIndex'
_L='TruthValue'
_K='OctetString'
_J='not-accessible'
_I='Integer32'
_H='read-only'
_G='A3COM-HUAWEI-FCOE-MIB'
_F='fcmInstanceIndex'
_E='FC-MGMT-MIB'
_D='read-write'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
fcmInstanceIndex,=mibBuilder.importSymbols(_E,_F)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_L)
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
h3cFCoE=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,120))
if mibBuilder.loadTexts:h3cFCoE.setRevisions(('2012-03-28 00:00',))
class H3cFCoEVfcBindType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('interfaceIndex',1),('macAddress',2)))
_H3cFCoEObjects_ObjectIdentity=ObjectIdentity
h3cFCoEObjects=_H3cFCoEObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,120,1))
_H3cFCoEConfig_ObjectIdentity=ObjectIdentity
h3cFCoEConfig=_H3cFCoEConfig_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,120,1,1))
_H3cFCoECfgTable_Object=MibTable
h3cFCoECfgTable=_H3cFCoECfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1))
if mibBuilder.loadTexts:h3cFCoECfgTable.setStatus(_A)
_H3cFCoECfgEntry_Object=MibTableRow
h3cFCoECfgEntry=_H3cFCoECfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1,1))
h3cFCoECfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cFCoECfgEntry.setStatus(_A)
class _H3cFCoECfgFcmap_Type(OctetString):defaultHexValue='0EFC00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_H3cFCoECfgFcmap_Type.__name__=_K
_H3cFCoECfgFcmap_Object=MibTableColumn
h3cFCoECfgFcmap=_H3cFCoECfgFcmap_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1,1,1),_H3cFCoECfgFcmap_Type())
h3cFCoECfgFcmap.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFCoECfgFcmap.setStatus(_A)
class _H3cFCoECfgDynamicVfcCreation_Type(TruthValue):defaultValue=2
_H3cFCoECfgDynamicVfcCreation_Type.__name__=_L
_H3cFCoECfgDynamicVfcCreation_Object=MibTableColumn
h3cFCoECfgDynamicVfcCreation=_H3cFCoECfgDynamicVfcCreation_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1,1,2),_H3cFCoECfgDynamicVfcCreation_Type())
h3cFCoECfgDynamicVfcCreation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFCoECfgDynamicVfcCreation.setStatus(_A)
class _H3cFCoECfgDefaultFCFPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cFCoECfgDefaultFCFPriority_Type.__name__=_C
_H3cFCoECfgDefaultFCFPriority_Object=MibTableColumn
h3cFCoECfgDefaultFCFPriority=_H3cFCoECfgDefaultFCFPriority_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1,1,3),_H3cFCoECfgDefaultFCFPriority_Type())
h3cFCoECfgDefaultFCFPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFCoECfgDefaultFCFPriority.setStatus(_A)
class _H3cFCoECfgDATov_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_H3cFCoECfgDATov_Type.__name__=_C
_H3cFCoECfgDATov_Object=MibTableColumn
h3cFCoECfgDATov=_H3cFCoECfgDATov_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1,1,4),_H3cFCoECfgDATov_Type())
h3cFCoECfgDATov.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFCoECfgDATov.setStatus(_A)
if mibBuilder.loadTexts:h3cFCoECfgDATov.setUnits('seconds')
class _H3cFCoECfgAddressingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fpma',1),('spma',2),('fpmaAndSpma',3)))
_H3cFCoECfgAddressingMode_Type.__name__=_I
_H3cFCoECfgAddressingMode_Object=MibTableColumn
h3cFCoECfgAddressingMode=_H3cFCoECfgAddressingMode_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,1,1,5),_H3cFCoECfgAddressingMode_Type())
h3cFCoECfgAddressingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFCoECfgAddressingMode.setStatus(_A)
_H3cFCoEVLANTable_Object=MibTable
h3cFCoEVLANTable=_H3cFCoEVLANTable_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,2))
if mibBuilder.loadTexts:h3cFCoEVLANTable.setStatus(_A)
_H3cFCoEVLANEntry_Object=MibTableRow
h3cFCoEVLANEntry=_H3cFCoEVLANEntry_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,2,1))
h3cFCoEVLANEntry.setIndexNames((0,_E,_F),(0,_G,_M),(0,_G,_N))
if mibBuilder.loadTexts:h3cFCoEVLANEntry.setStatus(_A)
_H3cFCoEVLANIndex_Type=VlanIndex
_H3cFCoEVLANIndex_Object=MibTableColumn
h3cFCoEVLANIndex=_H3cFCoEVLANIndex_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,2,1,1),_H3cFCoEVLANIndex_Type())
h3cFCoEVLANIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cFCoEVLANIndex.setStatus(_A)
_H3cFCoEFabricIndex_Type=T11FabricIndex
_H3cFCoEFabricIndex_Object=MibTableColumn
h3cFCoEFabricIndex=_H3cFCoEFabricIndex_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,2,1,2),_H3cFCoEFabricIndex_Type())
h3cFCoEFabricIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cFCoEFabricIndex.setStatus(_A)
class _H3cFCoEVLANOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_H3cFCoEVLANOperState_Type.__name__=_I
_H3cFCoEVLANOperState_Object=MibTableColumn
h3cFCoEVLANOperState=_H3cFCoEVLANOperState_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,2,1,3),_H3cFCoEVLANOperState_Type())
h3cFCoEVLANOperState.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFCoEVLANOperState.setStatus(_A)
_H3cFCoEVLANRowStatus_Type=RowStatus
_H3cFCoEVLANRowStatus_Object=MibTableColumn
h3cFCoEVLANRowStatus=_H3cFCoEVLANRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,2,1,4),_H3cFCoEVLANRowStatus_Type())
h3cFCoEVLANRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFCoEVLANRowStatus.setStatus(_A)
_H3cFCoEStaticVfcTable_Object=MibTable
h3cFCoEStaticVfcTable=_H3cFCoEStaticVfcTable_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3))
if mibBuilder.loadTexts:h3cFCoEStaticVfcTable.setStatus(_A)
_H3cFCoEStaticVfcEntry_Object=MibTableRow
h3cFCoEStaticVfcEntry=_H3cFCoEStaticVfcEntry_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1))
h3cFCoEStaticVfcEntry.setIndexNames((0,_E,_F),(0,_G,_O))
if mibBuilder.loadTexts:h3cFCoEStaticVfcEntry.setStatus(_A)
class _H3cFCoEStaticVfcIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cFCoEStaticVfcIndex_Type.__name__=_C
_H3cFCoEStaticVfcIndex_Object=MibTableColumn
h3cFCoEStaticVfcIndex=_H3cFCoEStaticVfcIndex_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,1),_H3cFCoEStaticVfcIndex_Type())
h3cFCoEStaticVfcIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cFCoEStaticVfcIndex.setStatus(_A)
class _H3cFCoEStaticVfcFCFPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cFCoEStaticVfcFCFPriority_Type.__name__=_C
_H3cFCoEStaticVfcFCFPriority_Object=MibTableColumn
h3cFCoEStaticVfcFCFPriority=_H3cFCoEStaticVfcFCFPriority_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,2),_H3cFCoEStaticVfcFCFPriority_Type())
h3cFCoEStaticVfcFCFPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFCoEStaticVfcFCFPriority.setStatus(_A)
_H3cFCoEStaticVfcBindType_Type=H3cFCoEVfcBindType
_H3cFCoEStaticVfcBindType_Object=MibTableColumn
h3cFCoEStaticVfcBindType=_H3cFCoEStaticVfcBindType_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,3),_H3cFCoEStaticVfcBindType_Type())
h3cFCoEStaticVfcBindType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFCoEStaticVfcBindType.setStatus(_A)
_H3cFCoEStaticVfcBindIfIndex_Type=InterfaceIndexOrZero
_H3cFCoEStaticVfcBindIfIndex_Object=MibTableColumn
h3cFCoEStaticVfcBindIfIndex=_H3cFCoEStaticVfcBindIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,4),_H3cFCoEStaticVfcBindIfIndex_Type())
h3cFCoEStaticVfcBindIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFCoEStaticVfcBindIfIndex.setStatus(_A)
_H3cFCoEStaticVfcBindMACAddress_Type=MacAddress
_H3cFCoEStaticVfcBindMACAddress_Object=MibTableColumn
h3cFCoEStaticVfcBindMACAddress=_H3cFCoEStaticVfcBindMACAddress_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,5),_H3cFCoEStaticVfcBindMACAddress_Type())
h3cFCoEStaticVfcBindMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFCoEStaticVfcBindMACAddress.setStatus(_A)
_H3cFCoEStaticVfcIfIndex_Type=InterfaceIndex
_H3cFCoEStaticVfcIfIndex_Object=MibTableColumn
h3cFCoEStaticVfcIfIndex=_H3cFCoEStaticVfcIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,6),_H3cFCoEStaticVfcIfIndex_Type())
h3cFCoEStaticVfcIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFCoEStaticVfcIfIndex.setStatus(_A)
_H3cFCoEStaticVfcCreationTime_Type=TimeStamp
_H3cFCoEStaticVfcCreationTime_Object=MibTableColumn
h3cFCoEStaticVfcCreationTime=_H3cFCoEStaticVfcCreationTime_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,7),_H3cFCoEStaticVfcCreationTime_Type())
h3cFCoEStaticVfcCreationTime.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFCoEStaticVfcCreationTime.setStatus(_A)
_H3cFCoEStaticVfcFailureCause_Type=SnmpAdminString
_H3cFCoEStaticVfcFailureCause_Object=MibTableColumn
h3cFCoEStaticVfcFailureCause=_H3cFCoEStaticVfcFailureCause_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,8),_H3cFCoEStaticVfcFailureCause_Type())
h3cFCoEStaticVfcFailureCause.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFCoEStaticVfcFailureCause.setStatus(_A)
_H3cFCoEStaticVfcRowStatus_Type=RowStatus
_H3cFCoEStaticVfcRowStatus_Object=MibTableColumn
h3cFCoEStaticVfcRowStatus=_H3cFCoEStaticVfcRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,120,1,1,3,1,9),_H3cFCoEStaticVfcRowStatus_Type())
h3cFCoEStaticVfcRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFCoEStaticVfcRowStatus.setStatus(_A)
_H3cFCoEFIPSnoopingObjects_ObjectIdentity=ObjectIdentity
h3cFCoEFIPSnoopingObjects=_H3cFCoEFIPSnoopingObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,120,1,2))
mibBuilder.exportSymbols(_G,**{'H3cFCoEVfcBindType':H3cFCoEVfcBindType,'h3cFCoE':h3cFCoE,'h3cFCoEObjects':h3cFCoEObjects,'h3cFCoEConfig':h3cFCoEConfig,'h3cFCoECfgTable':h3cFCoECfgTable,'h3cFCoECfgEntry':h3cFCoECfgEntry,'h3cFCoECfgFcmap':h3cFCoECfgFcmap,'h3cFCoECfgDynamicVfcCreation':h3cFCoECfgDynamicVfcCreation,'h3cFCoECfgDefaultFCFPriority':h3cFCoECfgDefaultFCFPriority,'h3cFCoECfgDATov':h3cFCoECfgDATov,'h3cFCoECfgAddressingMode':h3cFCoECfgAddressingMode,'h3cFCoEVLANTable':h3cFCoEVLANTable,'h3cFCoEVLANEntry':h3cFCoEVLANEntry,_M:h3cFCoEVLANIndex,_N:h3cFCoEFabricIndex,'h3cFCoEVLANOperState':h3cFCoEVLANOperState,'h3cFCoEVLANRowStatus':h3cFCoEVLANRowStatus,'h3cFCoEStaticVfcTable':h3cFCoEStaticVfcTable,'h3cFCoEStaticVfcEntry':h3cFCoEStaticVfcEntry,_O:h3cFCoEStaticVfcIndex,'h3cFCoEStaticVfcFCFPriority':h3cFCoEStaticVfcFCFPriority,'h3cFCoEStaticVfcBindType':h3cFCoEStaticVfcBindType,'h3cFCoEStaticVfcBindIfIndex':h3cFCoEStaticVfcBindIfIndex,'h3cFCoEStaticVfcBindMACAddress':h3cFCoEStaticVfcBindMACAddress,'h3cFCoEStaticVfcIfIndex':h3cFCoEStaticVfcIfIndex,'h3cFCoEStaticVfcCreationTime':h3cFCoEStaticVfcCreationTime,'h3cFCoEStaticVfcFailureCause':h3cFCoEStaticVfcFailureCause,'h3cFCoEStaticVfcRowStatus':h3cFCoEStaticVfcRowStatus,'h3cFCoEFIPSnoopingObjects':h3cFCoEFIPSnoopingObjects})