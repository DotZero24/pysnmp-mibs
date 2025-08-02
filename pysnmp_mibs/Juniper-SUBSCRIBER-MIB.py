_S='juniSubscriberLocalGroup2'
_R='juniSubscriberLocalGroup'
_Q='juniSubscrLocalAuthentication'
_P='obsolete'
_O='not-accessible'
_N='juniSubscrLocalEncaps'
_M='juniSubscrLocalIfIndex'
_L='Integer32'
_K='JuniEnable'
_J='juniSubscrLocalDomain'
_I='juniSubscrLocalPassword'
_H='juniSubscrLocalPasswordPrefix'
_G='juniSubscrLocalName'
_F='juniSubscrLocalNamePrefix'
_E='juniSubscrLocalControl'
_D='DisplayString'
_C='read-write'
_B='current'
_A='Juniper-SUBSCRIBER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
juniSubscriberMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,49))
if mibBuilder.loadTexts:juniSubscriberMIB.setRevisions(('2002-09-16 21:44','2002-05-10 19:53','2000-11-16 00:00'))
class JuniSubscrEncaps(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,19)));namedValues=NamedValues(*(('ip',0),('bridgedEthernet',19)))
_JuniSubscrObjects_ObjectIdentity=ObjectIdentity
juniSubscrObjects=_JuniSubscrObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,49,1))
_JuniSubscrLocal_ObjectIdentity=ObjectIdentity
juniSubscrLocal=_JuniSubscrLocal_ObjectIdentity((1,3,6,1,4,1,4874,2,2,49,1,1))
_JuniSubscrLocalTable_Object=MibTable
juniSubscrLocalTable=_JuniSubscrLocalTable_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1))
if mibBuilder.loadTexts:juniSubscrLocalTable.setStatus(_B)
_JuniSubscrLocalEntry_Object=MibTableRow
juniSubscrLocalEntry=_JuniSubscrLocalEntry_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1))
juniSubscrLocalEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:juniSubscrLocalEntry.setStatus(_B)
_JuniSubscrLocalIfIndex_Type=InterfaceIndex
_JuniSubscrLocalIfIndex_Object=MibTableColumn
juniSubscrLocalIfIndex=_JuniSubscrLocalIfIndex_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,1),_JuniSubscrLocalIfIndex_Type())
juniSubscrLocalIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:juniSubscrLocalIfIndex.setStatus(_B)
_JuniSubscrLocalEncaps_Type=JuniSubscrEncaps
_JuniSubscrLocalEncaps_Object=MibTableColumn
juniSubscrLocalEncaps=_JuniSubscrLocalEncaps_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,2),_JuniSubscrLocalEncaps_Type())
juniSubscrLocalEncaps.setMaxAccess(_O)
if mibBuilder.loadTexts:juniSubscrLocalEncaps.setStatus(_B)
class _JuniSubscrLocalControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),('clear',1)))
_JuniSubscrLocalControl_Type.__name__=_L
_JuniSubscrLocalControl_Object=MibTableColumn
juniSubscrLocalControl=_JuniSubscrLocalControl_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,3),_JuniSubscrLocalControl_Type())
juniSubscrLocalControl.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalControl.setStatus(_B)
_JuniSubscrLocalNamePrefix_Type=JuniEnable
_JuniSubscrLocalNamePrefix_Object=MibTableColumn
juniSubscrLocalNamePrefix=_JuniSubscrLocalNamePrefix_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,4),_JuniSubscrLocalNamePrefix_Type())
juniSubscrLocalNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalNamePrefix.setStatus(_B)
class _JuniSubscrLocalName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JuniSubscrLocalName_Type.__name__=_D
_JuniSubscrLocalName_Object=MibTableColumn
juniSubscrLocalName=_JuniSubscrLocalName_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,5),_JuniSubscrLocalName_Type())
juniSubscrLocalName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalName.setStatus(_B)
_JuniSubscrLocalPasswordPrefix_Type=JuniEnable
_JuniSubscrLocalPasswordPrefix_Object=MibTableColumn
juniSubscrLocalPasswordPrefix=_JuniSubscrLocalPasswordPrefix_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,6),_JuniSubscrLocalPasswordPrefix_Type())
juniSubscrLocalPasswordPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalPasswordPrefix.setStatus(_B)
class _JuniSubscrLocalPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JuniSubscrLocalPassword_Type.__name__=_D
_JuniSubscrLocalPassword_Object=MibTableColumn
juniSubscrLocalPassword=_JuniSubscrLocalPassword_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,7),_JuniSubscrLocalPassword_Type())
juniSubscrLocalPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalPassword.setStatus(_B)
class _JuniSubscrLocalDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JuniSubscrLocalDomain_Type.__name__=_D
_JuniSubscrLocalDomain_Object=MibTableColumn
juniSubscrLocalDomain=_JuniSubscrLocalDomain_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,8),_JuniSubscrLocalDomain_Type())
juniSubscrLocalDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalDomain.setStatus(_B)
class _JuniSubscrLocalAuthentication_Type(JuniEnable):defaultValue=1
_JuniSubscrLocalAuthentication_Type.__name__=_K
_JuniSubscrLocalAuthentication_Object=MibTableColumn
juniSubscrLocalAuthentication=_JuniSubscrLocalAuthentication_Object((1,3,6,1,4,1,4874,2,2,49,1,1,1,1,9),_JuniSubscrLocalAuthentication_Type())
juniSubscrLocalAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSubscrLocalAuthentication.setStatus(_B)
_JuniSubscriberMIBConformance_ObjectIdentity=ObjectIdentity
juniSubscriberMIBConformance=_JuniSubscriberMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,49,4))
_JuniSubscriberMIBCompliances_ObjectIdentity=ObjectIdentity
juniSubscriberMIBCompliances=_JuniSubscriberMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,49,4,1))
_JuniSubscriberMIBGroups_ObjectIdentity=ObjectIdentity
juniSubscriberMIBGroups=_JuniSubscriberMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,49,4,2))
juniSubscriberLocalGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,49,4,2,1))
juniSubscriberLocalGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:juniSubscriberLocalGroup.setStatus(_P)
juniSubscriberLocalGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,49,4,2,2))
juniSubscriberLocalGroup2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:juniSubscriberLocalGroup2.setStatus(_B)
juniSubscriberCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,49,4,1,1))
juniSubscriberCompliance.setObjects((_A,_R))
if mibBuilder.loadTexts:juniSubscriberCompliance.setStatus(_P)
juniSubscriberCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,49,4,1,2))
juniSubscriberCompliance2.setObjects((_A,_S))
if mibBuilder.loadTexts:juniSubscriberCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniSubscrEncaps':JuniSubscrEncaps,'juniSubscriberMIB':juniSubscriberMIB,'juniSubscrObjects':juniSubscrObjects,'juniSubscrLocal':juniSubscrLocal,'juniSubscrLocalTable':juniSubscrLocalTable,'juniSubscrLocalEntry':juniSubscrLocalEntry,_M:juniSubscrLocalIfIndex,_N:juniSubscrLocalEncaps,_E:juniSubscrLocalControl,_F:juniSubscrLocalNamePrefix,_G:juniSubscrLocalName,_H:juniSubscrLocalPasswordPrefix,_I:juniSubscrLocalPassword,_J:juniSubscrLocalDomain,_Q:juniSubscrLocalAuthentication,'juniSubscriberMIBConformance':juniSubscriberMIBConformance,'juniSubscriberMIBCompliances':juniSubscriberMIBCompliances,'juniSubscriberCompliance':juniSubscriberCompliance,'juniSubscriberCompliance2':juniSubscriberCompliance2,'juniSubscriberMIBGroups':juniSubscriberMIBGroups,_R:juniSubscriberLocalGroup,_S:juniSubscriberLocalGroup2})