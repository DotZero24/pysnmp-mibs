_L='arubaWiredProviderBridgeBaseGroup'
_K='arubaWiredProviderBridgeVlanType'
_J='arubaWiredProviderBridgePortType'
_I='arubaWiredProviderBridgeEtherType'
_H='arubaWiredProviderBridgeType'
_G='arubaWiredProviderBridgePortifIndex'
_F='not-accessible'
_E='arubaWiredProviderBridgeVlanTypeVlanID'
_D='read-only'
_C='Integer32'
_B='ARUBAWIRED-PROVIDER-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arubaWiredProviderBridgeMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,23))
if mibBuilder.loadTexts:arubaWiredProviderBridgeMIB.setRevisions(('2021-11-12 00:00',))
_ArubaWiredProviderBridgeNotifications_ObjectIdentity=ObjectIdentity
arubaWiredProviderBridgeNotifications=_ArubaWiredProviderBridgeNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,23,0))
_ArubaWiredProviderBridgeObjects_ObjectIdentity=ObjectIdentity
arubaWiredProviderBridgeObjects=_ArubaWiredProviderBridgeObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,23,1))
_ArubaWiredProviderBridgeBase_ObjectIdentity=ObjectIdentity
arubaWiredProviderBridgeBase=_ArubaWiredProviderBridgeBase_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,23,1,0))
class _ArubaWiredProviderBridgeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vlanBridge',1),('svlanBridge',2),('providerEdgeBridge',3),('vlanSvlanBridge',4)))
_ArubaWiredProviderBridgeType_Type.__name__=_C
_ArubaWiredProviderBridgeType_Object=MibScalar
arubaWiredProviderBridgeType=_ArubaWiredProviderBridgeType_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,1),_ArubaWiredProviderBridgeType_Type())
arubaWiredProviderBridgeType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredProviderBridgeType.setStatus(_A)
class _ArubaWiredProviderBridgeEtherType_Type(Integer32):defaultValue=34984;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_ArubaWiredProviderBridgeEtherType_Type.__name__=_C
_ArubaWiredProviderBridgeEtherType_Object=MibScalar
arubaWiredProviderBridgeEtherType=_ArubaWiredProviderBridgeEtherType_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,2),_ArubaWiredProviderBridgeEtherType_Type())
arubaWiredProviderBridgeEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredProviderBridgeEtherType.setStatus(_A)
_ArubaWiredProviderBridgeVlanTypeTable_Object=MibTable
arubaWiredProviderBridgeVlanTypeTable=_ArubaWiredProviderBridgeVlanTypeTable_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,3))
if mibBuilder.loadTexts:arubaWiredProviderBridgeVlanTypeTable.setStatus(_A)
_ArubaWiredProviderBridgeVlanTypeEntry_Object=MibTableRow
arubaWiredProviderBridgeVlanTypeEntry=_ArubaWiredProviderBridgeVlanTypeEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,3,1))
arubaWiredProviderBridgeVlanTypeEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:arubaWiredProviderBridgeVlanTypeEntry.setStatus(_A)
_ArubaWiredProviderBridgeVlanTypeVlanID_Type=VlanId
_ArubaWiredProviderBridgeVlanTypeVlanID_Object=MibTableColumn
arubaWiredProviderBridgeVlanTypeVlanID=_ArubaWiredProviderBridgeVlanTypeVlanID_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,3,1,1),_ArubaWiredProviderBridgeVlanTypeVlanID_Type())
arubaWiredProviderBridgeVlanTypeVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredProviderBridgeVlanTypeVlanID.setStatus(_A)
class _ArubaWiredProviderBridgeVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cvlan',1),('svlan',2)))
_ArubaWiredProviderBridgeVlanType_Type.__name__=_C
_ArubaWiredProviderBridgeVlanType_Object=MibTableColumn
arubaWiredProviderBridgeVlanType=_ArubaWiredProviderBridgeVlanType_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,3,1,2),_ArubaWiredProviderBridgeVlanType_Type())
arubaWiredProviderBridgeVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredProviderBridgeVlanType.setStatus(_A)
_ArubaWiredProviderBridgePortTable_Object=MibTable
arubaWiredProviderBridgePortTable=_ArubaWiredProviderBridgePortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,4))
if mibBuilder.loadTexts:arubaWiredProviderBridgePortTable.setStatus(_A)
_ArubaWiredProviderBridgePortEntry_Object=MibTableRow
arubaWiredProviderBridgePortEntry=_ArubaWiredProviderBridgePortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,4,1))
arubaWiredProviderBridgePortEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:arubaWiredProviderBridgePortEntry.setStatus(_A)
_ArubaWiredProviderBridgePortifIndex_Type=InterfaceIndex
_ArubaWiredProviderBridgePortifIndex_Object=MibTableColumn
arubaWiredProviderBridgePortifIndex=_ArubaWiredProviderBridgePortifIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,4,1,1),_ArubaWiredProviderBridgePortifIndex_Type())
arubaWiredProviderBridgePortifIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredProviderBridgePortifIndex.setStatus(_A)
class _ArubaWiredProviderBridgePortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('customerEdge',1),('customerNetwork',2),('providerNetwork',3)))
_ArubaWiredProviderBridgePortType_Type.__name__=_C
_ArubaWiredProviderBridgePortType_Object=MibTableColumn
arubaWiredProviderBridgePortType=_ArubaWiredProviderBridgePortType_Object((1,3,6,1,4,1,47196,4,1,1,3,23,1,0,4,1,2),_ArubaWiredProviderBridgePortType_Type())
arubaWiredProviderBridgePortType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredProviderBridgePortType.setStatus(_A)
_ArubaWiredProviderBridgeConformance_ObjectIdentity=ObjectIdentity
arubaWiredProviderBridgeConformance=_ArubaWiredProviderBridgeConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,23,2))
_ArubaWiredProviderBridgeCompliances_ObjectIdentity=ObjectIdentity
arubaWiredProviderBridgeCompliances=_ArubaWiredProviderBridgeCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,23,2,1))
_ArubaWiredProviderBridgeGroups_ObjectIdentity=ObjectIdentity
arubaWiredProviderBridgeGroups=_ArubaWiredProviderBridgeGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,23,2,2))
arubaWiredProviderBridgeBaseGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,23,2,2,1))
arubaWiredProviderBridgeBaseGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:arubaWiredProviderBridgeBaseGroup.setStatus(_A)
arubaWiredProviderBridgeCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,23,2,1,1))
arubaWiredProviderBridgeCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:arubaWiredProviderBridgeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredProviderBridgeMIB':arubaWiredProviderBridgeMIB,'arubaWiredProviderBridgeNotifications':arubaWiredProviderBridgeNotifications,'arubaWiredProviderBridgeObjects':arubaWiredProviderBridgeObjects,'arubaWiredProviderBridgeBase':arubaWiredProviderBridgeBase,_H:arubaWiredProviderBridgeType,_I:arubaWiredProviderBridgeEtherType,'arubaWiredProviderBridgeVlanTypeTable':arubaWiredProviderBridgeVlanTypeTable,'arubaWiredProviderBridgeVlanTypeEntry':arubaWiredProviderBridgeVlanTypeEntry,_E:arubaWiredProviderBridgeVlanTypeVlanID,_K:arubaWiredProviderBridgeVlanType,'arubaWiredProviderBridgePortTable':arubaWiredProviderBridgePortTable,'arubaWiredProviderBridgePortEntry':arubaWiredProviderBridgePortEntry,_G:arubaWiredProviderBridgePortifIndex,_J:arubaWiredProviderBridgePortType,'arubaWiredProviderBridgeConformance':arubaWiredProviderBridgeConformance,'arubaWiredProviderBridgeCompliances':arubaWiredProviderBridgeCompliances,'arubaWiredProviderBridgeCompliance':arubaWiredProviderBridgeCompliance,'arubaWiredProviderBridgeGroups':arubaWiredProviderBridgeGroups,_L:arubaWiredProviderBridgeBaseGroup})