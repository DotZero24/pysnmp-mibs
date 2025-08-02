_Q='ceaVlanGroup'
_P='ceaPortGroup'
_O='ceaUNIVlanType'
_N='ceaMaxUNIVlanCommunityPorts'
_M='ceaPortCapability'
_L='ceaPortType'
_K='ceaMaxNNIPorts'
_J='read-write'
_I='ifIndex'
_H='IF-MIB'
_G='vtpVlanIndex'
_F='managementDomainIndex'
_E='read-only'
_D='CISCO-VTP-MIB'
_C='Integer32'
_B='CISCO-ETHERNET-ACCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
managementDomainIndex,vtpVlanIndex=mibBuilder.importSymbols(_D,_F,_G)
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoEthernetAccessMIB=ModuleIdentity((1,3,6,1,4,1,9,9,466))
if mibBuilder.loadTexts:ciscoEthernetAccessMIB.setRevisions(('2007-09-14 00:00','2005-01-18 00:00'))
class CeaVlanUNIType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('isolated',2),('community',3)))
_CiscoEthernetAccessMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEthernetAccessMIBObjects=_CiscoEthernetAccessMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,466,1))
_CeaGlobals_ObjectIdentity=ObjectIdentity
ceaGlobals=_CeaGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,466,1,1))
class _CeaMaxNNIPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_CeaMaxNNIPorts_Type.__name__=_C
_CeaMaxNNIPorts_Object=MibScalar
ceaMaxNNIPorts=_CeaMaxNNIPorts_Object((1,3,6,1,4,1,9,9,466,1,1,1),_CeaMaxNNIPorts_Type())
ceaMaxNNIPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:ceaMaxNNIPorts.setStatus(_A)
class _CeaMaxUNIVlanCommunityPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_CeaMaxUNIVlanCommunityPorts_Type.__name__=_C
_CeaMaxUNIVlanCommunityPorts_Object=MibScalar
ceaMaxUNIVlanCommunityPorts=_CeaMaxUNIVlanCommunityPorts_Object((1,3,6,1,4,1,9,9,466,1,1,2),_CeaMaxUNIVlanCommunityPorts_Type())
ceaMaxUNIVlanCommunityPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:ceaMaxUNIVlanCommunityPorts.setStatus(_A)
_CeaConfig_ObjectIdentity=ObjectIdentity
ceaConfig=_CeaConfig_ObjectIdentity((1,3,6,1,4,1,9,9,466,1,2))
_CeaPortTable_Object=MibTable
ceaPortTable=_CeaPortTable_Object((1,3,6,1,4,1,9,9,466,1,2,1))
if mibBuilder.loadTexts:ceaPortTable.setStatus(_A)
_CeaPortEntry_Object=MibTableRow
ceaPortEntry=_CeaPortEntry_Object((1,3,6,1,4,1,9,9,466,1,2,1,1))
ceaPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ceaPortEntry.setStatus(_A)
class _CeaPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unspecified',1),('uni',2),('nni',3),('eni',4)))
_CeaPortType_Type.__name__=_C
_CeaPortType_Object=MibTableColumn
ceaPortType=_CeaPortType_Object((1,3,6,1,4,1,9,9,466,1,2,1,1,1),_CeaPortType_Type())
ceaPortType.setMaxAccess(_J)
if mibBuilder.loadTexts:ceaPortType.setStatus(_A)
class _CeaPortCapability_Type(Bits):namedValues=NamedValues(*(('nni',0),('uni',1),('eni',2)))
_CeaPortCapability_Type.__name__='Bits'
_CeaPortCapability_Object=MibTableColumn
ceaPortCapability=_CeaPortCapability_Object((1,3,6,1,4,1,9,9,466,1,2,1,1,2),_CeaPortCapability_Type())
ceaPortCapability.setMaxAccess(_E)
if mibBuilder.loadTexts:ceaPortCapability.setStatus(_A)
_CeaUNIVlanTable_Object=MibTable
ceaUNIVlanTable=_CeaUNIVlanTable_Object((1,3,6,1,4,1,9,9,466,1,2,2))
if mibBuilder.loadTexts:ceaUNIVlanTable.setStatus(_A)
_CeaUNIVlanEntry_Object=MibTableRow
ceaUNIVlanEntry=_CeaUNIVlanEntry_Object((1,3,6,1,4,1,9,9,466,1,2,2,1))
ceaUNIVlanEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:ceaUNIVlanEntry.setStatus(_A)
_CeaUNIVlanType_Type=CeaVlanUNIType
_CeaUNIVlanType_Object=MibTableColumn
ceaUNIVlanType=_CeaUNIVlanType_Object((1,3,6,1,4,1,9,9,466,1,2,2,1,1),_CeaUNIVlanType_Type())
ceaUNIVlanType.setMaxAccess(_J)
if mibBuilder.loadTexts:ceaUNIVlanType.setStatus(_A)
_CiscoEthernetAccessMIBConform_ObjectIdentity=ObjectIdentity
ciscoEthernetAccessMIBConform=_CiscoEthernetAccessMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,466,2))
_CEthernetAccessMIBCompliances_ObjectIdentity=ObjectIdentity
cEthernetAccessMIBCompliances=_CEthernetAccessMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,466,2,1))
_CEthernetAccessMIBGroups_ObjectIdentity=ObjectIdentity
cEthernetAccessMIBGroups=_CEthernetAccessMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,466,2,2))
ceaPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,466,2,2,1))
ceaPortGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ceaPortGroup.setStatus(_A)
ceaVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,466,2,2,2))
ceaVlanGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ceaVlanGroup.setStatus(_A)
cEthernetAccessMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,466,2,1,1))
cEthernetAccessMIBCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cEthernetAccessMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CeaVlanUNIType':CeaVlanUNIType,'ciscoEthernetAccessMIB':ciscoEthernetAccessMIB,'ciscoEthernetAccessMIBObjects':ciscoEthernetAccessMIBObjects,'ceaGlobals':ceaGlobals,_K:ceaMaxNNIPorts,_N:ceaMaxUNIVlanCommunityPorts,'ceaConfig':ceaConfig,'ceaPortTable':ceaPortTable,'ceaPortEntry':ceaPortEntry,_L:ceaPortType,_M:ceaPortCapability,'ceaUNIVlanTable':ceaUNIVlanTable,'ceaUNIVlanEntry':ceaUNIVlanEntry,_O:ceaUNIVlanType,'ciscoEthernetAccessMIBConform':ciscoEthernetAccessMIBConform,'cEthernetAccessMIBCompliances':cEthernetAccessMIBCompliances,'cEthernetAccessMIBCompliance':cEthernetAccessMIBCompliance,'cEthernetAccessMIBGroups':cEthernetAccessMIBGroups,_P:ceaPortGroup,_Q:ceaVlanGroup})