_R='juniTsmGroup'
_Q='juniTsmApplicationActiveInterfaces'
_P='juniTsmApplicationMaxInterfaces'
_O='juniTsmAppRegistryInterfaceLimit'
_N='juniTsmAppRegistryName'
_M='juniTsmAppRegistryIfType'
_L='juniTsmPortProvisionedInterfaces'
_K='juniTsmPortAvailableInterfaces'
_J='juniTsmPortHwPresent'
_I='juniTsmPortType'
_H='juniTsmLocationType'
_G='not-accessible'
_F='juniTsmAppRegistryIndex'
_E='juniTsmPortLocation'
_D='Integer32'
_C='read-only'
_B='Juniper-TSM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniIfType,=mibBuilder.importSymbols('Juniper-UNI-IF-MIB','JuniIfType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
juniTsmMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,72))
if mibBuilder.loadTexts:juniTsmMIB.setRevisions(('2005-05-23 14:37','2005-04-27 22:57','2003-10-23 20:45'))
class JuniTsmLocationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('slotPort',1),('slotAdapterPort',2),('adapterPort',3)))
class JuniTsmLocationValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_JuniTsmObjects_ObjectIdentity=ObjectIdentity
juniTsmObjects=_JuniTsmObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,72,1))
_JuniTsmData_ObjectIdentity=ObjectIdentity
juniTsmData=_JuniTsmData_ObjectIdentity((1,3,6,1,4,1,4874,2,2,72,1,1))
_JuniTsmLocationType_Type=JuniTsmLocationType
_JuniTsmLocationType_Object=MibScalar
juniTsmLocationType=_JuniTsmLocationType_Object((1,3,6,1,4,1,4874,2,2,72,1,1,1),_JuniTsmLocationType_Type())
juniTsmLocationType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmLocationType.setStatus(_A)
_JuniTsmPortTable_Object=MibTable
juniTsmPortTable=_JuniTsmPortTable_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2))
if mibBuilder.loadTexts:juniTsmPortTable.setStatus(_A)
_JuniTsmPortEntry_Object=MibTableRow
juniTsmPortEntry=_JuniTsmPortEntry_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2,1))
juniTsmPortEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:juniTsmPortEntry.setStatus(_A)
_JuniTsmPortLocation_Type=JuniTsmLocationValue
_JuniTsmPortLocation_Object=MibTableColumn
juniTsmPortLocation=_JuniTsmPortLocation_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2,1,1),_JuniTsmPortLocation_Type())
juniTsmPortLocation.setMaxAccess(_G)
if mibBuilder.loadTexts:juniTsmPortLocation.setStatus(_A)
class _JuniTsmPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('generalPurposeStatic',1),('generalPurposeDynamic',2),('securityStatic',3),('securityDynamic',4)))
_JuniTsmPortType_Type.__name__=_D
_JuniTsmPortType_Object=MibTableColumn
juniTsmPortType=_JuniTsmPortType_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2,1,2),_JuniTsmPortType_Type())
juniTsmPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmPortType.setStatus(_A)
_JuniTsmPortHwPresent_Type=TruthValue
_JuniTsmPortHwPresent_Object=MibTableColumn
juniTsmPortHwPresent=_JuniTsmPortHwPresent_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2,1,3),_JuniTsmPortHwPresent_Type())
juniTsmPortHwPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmPortHwPresent.setStatus(_A)
class _JuniTsmPortAvailableInterfaces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16000))
_JuniTsmPortAvailableInterfaces_Type.__name__=_D
_JuniTsmPortAvailableInterfaces_Object=MibTableColumn
juniTsmPortAvailableInterfaces=_JuniTsmPortAvailableInterfaces_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2,1,4),_JuniTsmPortAvailableInterfaces_Type())
juniTsmPortAvailableInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmPortAvailableInterfaces.setStatus(_A)
class _JuniTsmPortProvisionedInterfaces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,16000))
_JuniTsmPortProvisionedInterfaces_Type.__name__=_D
_JuniTsmPortProvisionedInterfaces_Object=MibTableColumn
juniTsmPortProvisionedInterfaces=_JuniTsmPortProvisionedInterfaces_Object((1,3,6,1,4,1,4874,2,2,72,1,1,2,1,5),_JuniTsmPortProvisionedInterfaces_Type())
juniTsmPortProvisionedInterfaces.setMaxAccess('read-write')
if mibBuilder.loadTexts:juniTsmPortProvisionedInterfaces.setStatus(_A)
_JuniTsmAppRegistryTable_Object=MibTable
juniTsmAppRegistryTable=_JuniTsmAppRegistryTable_Object((1,3,6,1,4,1,4874,2,2,72,1,1,3))
if mibBuilder.loadTexts:juniTsmAppRegistryTable.setStatus(_A)
_JuniTsmAppRegistryEntry_Object=MibTableRow
juniTsmAppRegistryEntry=_JuniTsmAppRegistryEntry_Object((1,3,6,1,4,1,4874,2,2,72,1,1,3,1))
juniTsmAppRegistryEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:juniTsmAppRegistryEntry.setStatus(_A)
class _JuniTsmAppRegistryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniTsmAppRegistryIndex_Type.__name__=_D
_JuniTsmAppRegistryIndex_Object=MibTableColumn
juniTsmAppRegistryIndex=_JuniTsmAppRegistryIndex_Object((1,3,6,1,4,1,4874,2,2,72,1,1,3,1,1),_JuniTsmAppRegistryIndex_Type())
juniTsmAppRegistryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniTsmAppRegistryIndex.setStatus(_A)
_JuniTsmAppRegistryIfType_Type=JuniIfType
_JuniTsmAppRegistryIfType_Object=MibTableColumn
juniTsmAppRegistryIfType=_JuniTsmAppRegistryIfType_Object((1,3,6,1,4,1,4874,2,2,72,1,1,3,1,2),_JuniTsmAppRegistryIfType_Type())
juniTsmAppRegistryIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmAppRegistryIfType.setStatus(_A)
_JuniTsmAppRegistryName_Type=DisplayString
_JuniTsmAppRegistryName_Object=MibTableColumn
juniTsmAppRegistryName=_JuniTsmAppRegistryName_Object((1,3,6,1,4,1,4874,2,2,72,1,1,3,1,3),_JuniTsmAppRegistryName_Type())
juniTsmAppRegistryName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmAppRegistryName.setStatus(_A)
class _JuniTsmAppRegistryInterfaceLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniTsmAppRegistryInterfaceLimit_Type.__name__=_D
_JuniTsmAppRegistryInterfaceLimit_Object=MibTableColumn
juniTsmAppRegistryInterfaceLimit=_JuniTsmAppRegistryInterfaceLimit_Object((1,3,6,1,4,1,4874,2,2,72,1,1,3,1,4),_JuniTsmAppRegistryInterfaceLimit_Type())
juniTsmAppRegistryInterfaceLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmAppRegistryInterfaceLimit.setStatus(_A)
_JuniTsmApplicationTable_Object=MibTable
juniTsmApplicationTable=_JuniTsmApplicationTable_Object((1,3,6,1,4,1,4874,2,2,72,1,1,4))
if mibBuilder.loadTexts:juniTsmApplicationTable.setStatus(_A)
_JuniTsmApplicationEntry_Object=MibTableRow
juniTsmApplicationEntry=_JuniTsmApplicationEntry_Object((1,3,6,1,4,1,4874,2,2,72,1,1,4,1))
juniTsmApplicationEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:juniTsmApplicationEntry.setStatus(_A)
class _JuniTsmApplicationMaxInterfaces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniTsmApplicationMaxInterfaces_Type.__name__=_D
_JuniTsmApplicationMaxInterfaces_Object=MibTableColumn
juniTsmApplicationMaxInterfaces=_JuniTsmApplicationMaxInterfaces_Object((1,3,6,1,4,1,4874,2,2,72,1,1,4,1,1),_JuniTsmApplicationMaxInterfaces_Type())
juniTsmApplicationMaxInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmApplicationMaxInterfaces.setStatus(_A)
_JuniTsmApplicationActiveInterfaces_Type=Gauge32
_JuniTsmApplicationActiveInterfaces_Object=MibTableColumn
juniTsmApplicationActiveInterfaces=_JuniTsmApplicationActiveInterfaces_Object((1,3,6,1,4,1,4874,2,2,72,1,1,4,1,2),_JuniTsmApplicationActiveInterfaces_Type())
juniTsmApplicationActiveInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTsmApplicationActiveInterfaces.setStatus(_A)
_JuniTsmMIBConformance_ObjectIdentity=ObjectIdentity
juniTsmMIBConformance=_JuniTsmMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,72,4))
_JuniTsmMIBCompliances_ObjectIdentity=ObjectIdentity
juniTsmMIBCompliances=_JuniTsmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,72,4,1))
_JuniTsmMIBGroups_ObjectIdentity=ObjectIdentity
juniTsmMIBGroups=_JuniTsmMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,72,4,2))
juniTsmGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,72,4,2,1))
juniTsmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:juniTsmGroup.setStatus(_A)
juniTsmCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,72,4,1,1))
juniTsmCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:juniTsmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniTsmLocationType':JuniTsmLocationType,'JuniTsmLocationValue':JuniTsmLocationValue,'juniTsmMIB':juniTsmMIB,'juniTsmObjects':juniTsmObjects,'juniTsmData':juniTsmData,_H:juniTsmLocationType,'juniTsmPortTable':juniTsmPortTable,'juniTsmPortEntry':juniTsmPortEntry,_E:juniTsmPortLocation,_I:juniTsmPortType,_J:juniTsmPortHwPresent,_K:juniTsmPortAvailableInterfaces,_L:juniTsmPortProvisionedInterfaces,'juniTsmAppRegistryTable':juniTsmAppRegistryTable,'juniTsmAppRegistryEntry':juniTsmAppRegistryEntry,_F:juniTsmAppRegistryIndex,_M:juniTsmAppRegistryIfType,_N:juniTsmAppRegistryName,_O:juniTsmAppRegistryInterfaceLimit,'juniTsmApplicationTable':juniTsmApplicationTable,'juniTsmApplicationEntry':juniTsmApplicationEntry,_P:juniTsmApplicationMaxInterfaces,_Q:juniTsmApplicationActiveInterfaces,'juniTsmMIBConformance':juniTsmMIBConformance,'juniTsmMIBCompliances':juniTsmMIBCompliances,'juniTsmCompliance':juniTsmCompliance,'juniTsmMIBGroups':juniTsmMIBGroups,_R:juniTsmGroup})