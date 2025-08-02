_P='cmabClientInfoGroup'
_O='cmabIfConfigGroup'
_N='cmabClientAuthStatus'
_M='cmabClientMabState'
_L='cmabClientMacAddress'
_K='cmabIfAuthMethod'
_J='cmabIfAuthEnabled'
_I='cmabClientSessionId'
_H='read-write'
_G='OctetString'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='CISCO-MAC-AUTH-BYPASS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ciscoMabMIB=ModuleIdentity((1,3,6,1,4,1,9,9,654))
if mibBuilder.loadTexts:ciscoMabMIB.setRevisions(('2008-04-18 00:00',))
_CmabNotification_ObjectIdentity=ObjectIdentity
cmabNotification=_CmabNotification_ObjectIdentity((1,3,6,1,4,1,9,9,654,0))
_CmabMIBObjects_ObjectIdentity=ObjectIdentity
cmabMIBObjects=_CmabMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,654,1))
_CmabInterfaceConfig_ObjectIdentity=ObjectIdentity
cmabInterfaceConfig=_CmabInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,654,1,1))
_CmabIfConfigTable_Object=MibTable
cmabIfConfigTable=_CmabIfConfigTable_Object((1,3,6,1,4,1,9,9,654,1,1,1))
if mibBuilder.loadTexts:cmabIfConfigTable.setStatus(_A)
_CmabIfConfigEntry_Object=MibTableRow
cmabIfConfigEntry=_CmabIfConfigEntry_Object((1,3,6,1,4,1,9,9,654,1,1,1,1))
cmabIfConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cmabIfConfigEntry.setStatus(_A)
_CmabIfAuthEnabled_Type=TruthValue
_CmabIfAuthEnabled_Object=MibTableColumn
cmabIfAuthEnabled=_CmabIfAuthEnabled_Object((1,3,6,1,4,1,9,9,654,1,1,1,1,1),_CmabIfAuthEnabled_Type())
cmabIfAuthEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:cmabIfAuthEnabled.setStatus(_A)
class _CmabIfAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('radius',1),('eap',2)))
_CmabIfAuthMethod_Type.__name__=_C
_CmabIfAuthMethod_Object=MibTableColumn
cmabIfAuthMethod=_CmabIfAuthMethod_Object((1,3,6,1,4,1,9,9,654,1,1,1,1,2),_CmabIfAuthMethod_Type())
cmabIfAuthMethod.setMaxAccess(_H)
if mibBuilder.loadTexts:cmabIfAuthMethod.setStatus(_A)
_CmabSession_ObjectIdentity=ObjectIdentity
cmabSession=_CmabSession_ObjectIdentity((1,3,6,1,4,1,9,9,654,1,2))
_CmabClientInfoTable_Object=MibTable
cmabClientInfoTable=_CmabClientInfoTable_Object((1,3,6,1,4,1,9,9,654,1,2,1))
if mibBuilder.loadTexts:cmabClientInfoTable.setStatus(_A)
_CmabClientInfoEntry_Object=MibTableRow
cmabClientInfoEntry=_CmabClientInfoEntry_Object((1,3,6,1,4,1,9,9,654,1,2,1,1))
cmabClientInfoEntry.setIndexNames((0,_D,_E),(1,_B,_I))
if mibBuilder.loadTexts:cmabClientInfoEntry.setStatus(_A)
class _CmabClientSessionId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CmabClientSessionId_Type.__name__=_G
_CmabClientSessionId_Object=MibTableColumn
cmabClientSessionId=_CmabClientSessionId_Object((1,3,6,1,4,1,9,9,654,1,2,1,1,1),_CmabClientSessionId_Type())
cmabClientSessionId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cmabClientSessionId.setStatus(_A)
_CmabClientMacAddress_Type=MacAddress
_CmabClientMacAddress_Object=MibTableColumn
cmabClientMacAddress=_CmabClientMacAddress_Object((1,3,6,1,4,1,9,9,654,1,2,1,1,2),_CmabClientMacAddress_Type())
cmabClientMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cmabClientMacAddress.setStatus(_A)
class _CmabClientMabState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('initialize',2),('acquiring',3),('authorizing',4),('terminate',5)))
_CmabClientMabState_Type.__name__=_C
_CmabClientMabState_Object=MibTableColumn
cmabClientMabState=_CmabClientMabState_Object((1,3,6,1,4,1,9,9,654,1,2,1,1,3),_CmabClientMabState_Type())
cmabClientMabState.setMaxAccess(_F)
if mibBuilder.loadTexts:cmabClientMabState.setStatus(_A)
class _CmabClientAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
_CmabClientAuthStatus_Type.__name__=_C
_CmabClientAuthStatus_Object=MibTableColumn
cmabClientAuthStatus=_CmabClientAuthStatus_Object((1,3,6,1,4,1,9,9,654,1,2,1,1,4),_CmabClientAuthStatus_Type())
cmabClientAuthStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cmabClientAuthStatus.setStatus(_A)
_CmabMIBConformance_ObjectIdentity=ObjectIdentity
cmabMIBConformance=_CmabMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,654,2))
_CmabMIBCompliances_ObjectIdentity=ObjectIdentity
cmabMIBCompliances=_CmabMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,654,2,1))
_CmabMIBGroups_ObjectIdentity=ObjectIdentity
cmabMIBGroups=_CmabMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,654,2,2))
cmabIfConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,654,2,2,1))
cmabIfConfigGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cmabIfConfigGroup.setStatus(_A)
cmabClientInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,654,2,2,2))
cmabClientInfoGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cmabClientInfoGroup.setStatus(_A)
cmabCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,654,2,1,1))
cmabCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cmabCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoMabMIB':ciscoMabMIB,'cmabNotification':cmabNotification,'cmabMIBObjects':cmabMIBObjects,'cmabInterfaceConfig':cmabInterfaceConfig,'cmabIfConfigTable':cmabIfConfigTable,'cmabIfConfigEntry':cmabIfConfigEntry,_J:cmabIfAuthEnabled,_K:cmabIfAuthMethod,'cmabSession':cmabSession,'cmabClientInfoTable':cmabClientInfoTable,'cmabClientInfoEntry':cmabClientInfoEntry,_I:cmabClientSessionId,_L:cmabClientMacAddress,_M:cmabClientMabState,_N:cmabClientAuthStatus,'cmabMIBConformance':cmabMIBConformance,'cmabMIBCompliances':cmabMIBCompliances,'cmabCompliance':cmabCompliance,'cmabMIBGroups':cmabMIBGroups,_O:cmabIfConfigGroup,_P:cmabClientInfoGroup})