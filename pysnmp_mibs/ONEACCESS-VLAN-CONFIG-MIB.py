_I='outerSPVlan'
_H='ONEACCESS-VLAN-CONFIG-MIB'
_G='Unsigned32'
_F='OctetString'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
oacExpIMIp,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIp','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
oaVlanConfigMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,681))
if mibBuilder.loadTexts:oaVlanConfigMIB.setRevisions(('2011-06-15 00:00','2010-07-08 00:01'))
class SPVlanEtherType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('etherType-8100',1),('etherType-9100',2),('etherType-88a8',3)))
_OacVlanConfig_ObjectIdentity=ObjectIdentity
oacVlanConfig=_OacVlanConfig_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,6))
_OacVlanConfigObjects_ObjectIdentity=ObjectIdentity
oacVlanConfigObjects=_OacVlanConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,6,1))
_OacVlanMappingConfigInterfaceObjects_ObjectIdentity=ObjectIdentity
oacVlanMappingConfigInterfaceObjects=_OacVlanMappingConfigInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,6,1,1))
_OacVlanConfigInterfaceTable_Object=MibTable
oacVlanConfigInterfaceTable=_OacVlanConfigInterfaceTable_Object((1,3,6,1,4,1,13191,10,3,1,6,1,1,1))
if mibBuilder.loadTexts:oacVlanConfigInterfaceTable.setStatus(_A)
_OacVlanConfigInterfaceEntry_Object=MibTableRow
oacVlanConfigInterfaceEntry=_OacVlanConfigInterfaceEntry_Object((1,3,6,1,4,1,13191,10,3,1,6,1,1,1,1))
oacVlanConfigInterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oacVlanConfigInterfaceEntry.setStatus(_A)
class _OacVlanConfigInterfaceDot1qValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_OacVlanConfigInterfaceDot1qValue_Type.__name__=_C
_OacVlanConfigInterfaceDot1qValue_Object=MibTableColumn
oacVlanConfigInterfaceDot1qValue=_OacVlanConfigInterfaceDot1qValue_Object((1,3,6,1,4,1,13191,10,3,1,6,1,1,1,1,1),_OacVlanConfigInterfaceDot1qValue_Type())
oacVlanConfigInterfaceDot1qValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacVlanConfigInterfaceDot1qValue.setStatus(_A)
class _OacVlanConfigInterfaceSecondDot1qValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_OacVlanConfigInterfaceSecondDot1qValue_Type.__name__=_C
_OacVlanConfigInterfaceSecondDot1qValue_Object=MibTableColumn
oacVlanConfigInterfaceSecondDot1qValue=_OacVlanConfigInterfaceSecondDot1qValue_Object((1,3,6,1,4,1,13191,10,3,1,6,1,1,1,1,2),_OacVlanConfigInterfaceSecondDot1qValue_Type())
oacVlanConfigInterfaceSecondDot1qValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacVlanConfigInterfaceSecondDot1qValue.setStatus(_A)
class _OacVlanConfigInterfaceDefaultPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OacVlanConfigInterfaceDefaultPriority_Type.__name__=_C
_OacVlanConfigInterfaceDefaultPriority_Object=MibTableColumn
oacVlanConfigInterfaceDefaultPriority=_OacVlanConfigInterfaceDefaultPriority_Object((1,3,6,1,4,1,13191,10,3,1,6,1,1,1,1,3),_OacVlanConfigInterfaceDefaultPriority_Type())
oacVlanConfigInterfaceDefaultPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oacVlanConfigInterfaceDefaultPriority.setStatus(_A)
_OacVlanConfigInterfaceRowStatus_Type=RowStatus
_OacVlanConfigInterfaceRowStatus_Object=MibTableColumn
oacVlanConfigInterfaceRowStatus=_OacVlanConfigInterfaceRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,6,1,1,1,1,4),_OacVlanConfigInterfaceRowStatus_Type())
oacVlanConfigInterfaceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacVlanConfigInterfaceRowStatus.setStatus(_A)
_OacVlanMappingConfigObjects_ObjectIdentity=ObjectIdentity
oacVlanMappingConfigObjects=_OacVlanMappingConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,6,1,2))
_VlanMappingTable_Object=MibTable
vlanMappingTable=_VlanMappingTable_Object((1,3,6,1,4,1,13191,10,3,1,6,1,2,1))
if mibBuilder.loadTexts:vlanMappingTable.setStatus(_A)
_VlanMappingEntry_Object=MibTableRow
vlanMappingEntry=_VlanMappingEntry_Object((1,3,6,1,4,1,13191,10,3,1,6,1,2,1,1))
vlanMappingEntry.setIndexNames((0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:vlanMappingEntry.setStatus(_A)
class _InnerCVlan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_InnerCVlan_Type.__name__=_F
_InnerCVlan_Object=MibTableColumn
innerCVlan=_InnerCVlan_Object((1,3,6,1,4,1,13191,10,3,1,6,1,2,1,1,1),_InnerCVlan_Type())
innerCVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:innerCVlan.setStatus(_A)
class _OuterSPVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_OuterSPVlan_Type.__name__=_G
_OuterSPVlan_Object=MibTableColumn
outerSPVlan=_OuterSPVlan_Object((1,3,6,1,4,1,13191,10,3,1,6,1,2,1,1,2),_OuterSPVlan_Type())
outerSPVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:outerSPVlan.setStatus(_A)
_OuterEtherType_Type=SPVlanEtherType
_OuterEtherType_Object=MibTableColumn
outerEtherType=_OuterEtherType_Object((1,3,6,1,4,1,13191,10,3,1,6,1,2,1,1,3),_OuterEtherType_Type())
outerEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:outerEtherType.setStatus(_A)
_VlanMappingRowStatus_Type=RowStatus
_VlanMappingRowStatus_Object=MibTableColumn
vlanMappingRowStatus=_VlanMappingRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,6,1,2,1,1,4),_VlanMappingRowStatus_Type())
vlanMappingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMappingRowStatus.setStatus(_A)
_OacVlanConfigConformance_ObjectIdentity=ObjectIdentity
oacVlanConfigConformance=_OacVlanConfigConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,6,2))
mibBuilder.exportSymbols(_H,**{'SPVlanEtherType':SPVlanEtherType,'oaVlanConfigMIB':oaVlanConfigMIB,'oacVlanConfig':oacVlanConfig,'oacVlanConfigObjects':oacVlanConfigObjects,'oacVlanMappingConfigInterfaceObjects':oacVlanMappingConfigInterfaceObjects,'oacVlanConfigInterfaceTable':oacVlanConfigInterfaceTable,'oacVlanConfigInterfaceEntry':oacVlanConfigInterfaceEntry,'oacVlanConfigInterfaceDot1qValue':oacVlanConfigInterfaceDot1qValue,'oacVlanConfigInterfaceSecondDot1qValue':oacVlanConfigInterfaceSecondDot1qValue,'oacVlanConfigInterfaceDefaultPriority':oacVlanConfigInterfaceDefaultPriority,'oacVlanConfigInterfaceRowStatus':oacVlanConfigInterfaceRowStatus,'oacVlanMappingConfigObjects':oacVlanMappingConfigObjects,'vlanMappingTable':vlanMappingTable,'vlanMappingEntry':vlanMappingEntry,'innerCVlan':innerCVlan,_I:outerSPVlan,'outerEtherType':outerEtherType,'vlanMappingRowStatus':vlanMappingRowStatus,'oacVlanConfigConformance':oacVlanConfigConformance})