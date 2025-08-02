_V='colubrisAAAClientMIBGroup'
_U='colubrisAAAProfileMIBGroup'
_T='colubrisAAANASId'
_S='colubrisAAATimeout'
_R='colubrisAAAAccountingPort'
_Q='colubrisAAAAuthenticationPort'
_P='colubrisAAASharedSecret'
_O='colubrisAAAServerName'
_N='colubrisAAAAuthenMethod'
_M='colubrisAAAAuthenProtocol'
_L='colubrisAAAProfileSecondaryServerIndex'
_K='colubrisAAAProfilePrimaryServerIndex'
_J='colubrisAAAProfileName'
_I='colubrisAAAServerIndex'
_H='not-accessible'
_G='colubrisAAAProfileIndex'
_F='read-write'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-AAA-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisProfileIndex,ColubrisServerIndex,ColubrisServerIndexOrZero=mibBuilder.importSymbols('COLUBRIS-TC','ColubrisProfileIndex','ColubrisServerIndex','ColubrisServerIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisAAAClientMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,5))
_ColubrisAAAClientObjects_ObjectIdentity=ObjectIdentity
colubrisAAAClientObjects=_ColubrisAAAClientObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,5,1))
_ColubrisAAAProfileGroup_ObjectIdentity=ObjectIdentity
colubrisAAAProfileGroup=_ColubrisAAAProfileGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,5,1,1))
_ColubrisAAAProfileTable_Object=MibTable
colubrisAAAProfileTable=_ColubrisAAAProfileTable_Object((1,3,6,1,4,1,8744,5,5,1,1,1))
if mibBuilder.loadTexts:colubrisAAAProfileTable.setStatus(_A)
_ColubrisAAAProfileEntry_Object=MibTableRow
colubrisAAAProfileEntry=_ColubrisAAAProfileEntry_Object((1,3,6,1,4,1,8744,5,5,1,1,1,1))
colubrisAAAProfileEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:colubrisAAAProfileEntry.setStatus(_A)
_ColubrisAAAProfileIndex_Type=ColubrisProfileIndex
_ColubrisAAAProfileIndex_Object=MibTableColumn
colubrisAAAProfileIndex=_ColubrisAAAProfileIndex_Object((1,3,6,1,4,1,8744,5,5,1,1,1,1,1),_ColubrisAAAProfileIndex_Type())
colubrisAAAProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:colubrisAAAProfileIndex.setStatus(_A)
_ColubrisAAAProfileName_Type=DisplayString
_ColubrisAAAProfileName_Object=MibTableColumn
colubrisAAAProfileName=_ColubrisAAAProfileName_Object((1,3,6,1,4,1,8744,5,5,1,1,1,1,2),_ColubrisAAAProfileName_Type())
colubrisAAAProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:colubrisAAAProfileName.setStatus(_A)
_ColubrisAAAProfilePrimaryServerIndex_Type=ColubrisServerIndexOrZero
_ColubrisAAAProfilePrimaryServerIndex_Object=MibTableColumn
colubrisAAAProfilePrimaryServerIndex=_ColubrisAAAProfilePrimaryServerIndex_Object((1,3,6,1,4,1,8744,5,5,1,1,1,1,3),_ColubrisAAAProfilePrimaryServerIndex_Type())
colubrisAAAProfilePrimaryServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAAProfilePrimaryServerIndex.setStatus(_A)
_ColubrisAAAProfileSecondaryServerIndex_Type=ColubrisServerIndexOrZero
_ColubrisAAAProfileSecondaryServerIndex_Object=MibTableColumn
colubrisAAAProfileSecondaryServerIndex=_ColubrisAAAProfileSecondaryServerIndex_Object((1,3,6,1,4,1,8744,5,5,1,1,1,1,4),_ColubrisAAAProfileSecondaryServerIndex_Type())
colubrisAAAProfileSecondaryServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAAProfileSecondaryServerIndex.setStatus(_A)
_ColubrisAAAServerGroup_ObjectIdentity=ObjectIdentity
colubrisAAAServerGroup=_ColubrisAAAServerGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,5,1,2))
_ColubrisAAAServerTable_Object=MibTable
colubrisAAAServerTable=_ColubrisAAAServerTable_Object((1,3,6,1,4,1,8744,5,5,1,2,1))
if mibBuilder.loadTexts:colubrisAAAServerTable.setStatus(_A)
_ColubrisAAAServerEntry_Object=MibTableRow
colubrisAAAServerEntry=_ColubrisAAAServerEntry_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1))
colubrisAAAServerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:colubrisAAAServerEntry.setStatus(_A)
_ColubrisAAAServerIndex_Type=ColubrisServerIndex
_ColubrisAAAServerIndex_Object=MibTableColumn
colubrisAAAServerIndex=_ColubrisAAAServerIndex_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,1),_ColubrisAAAServerIndex_Type())
colubrisAAAServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:colubrisAAAServerIndex.setStatus(_A)
class _ColubrisAAAAuthenProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('radius',1))
_ColubrisAAAAuthenProtocol_Type.__name__=_D
_ColubrisAAAAuthenProtocol_Object=MibTableColumn
colubrisAAAAuthenProtocol=_ColubrisAAAAuthenProtocol_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,2),_ColubrisAAAAuthenProtocol_Type())
colubrisAAAAuthenProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAAAuthenProtocol.setStatus(_A)
class _ColubrisAAAAuthenMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pap',1),('chap',2),('mschap',3),('mschapv2',4),('eapMd5',5)))
_ColubrisAAAAuthenMethod_Type.__name__=_D
_ColubrisAAAAuthenMethod_Object=MibTableColumn
colubrisAAAAuthenMethod=_ColubrisAAAAuthenMethod_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,3),_ColubrisAAAAuthenMethod_Type())
colubrisAAAAuthenMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAAAuthenMethod.setStatus(_A)
class _ColubrisAAAServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ColubrisAAAServerName_Type.__name__=_E
_ColubrisAAAServerName_Object=MibTableColumn
colubrisAAAServerName=_ColubrisAAAServerName_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,4),_ColubrisAAAServerName_Type())
colubrisAAAServerName.setMaxAccess(_F)
if mibBuilder.loadTexts:colubrisAAAServerName.setStatus(_A)
_ColubrisAAASharedSecret_Type=DisplayString
_ColubrisAAASharedSecret_Object=MibTableColumn
colubrisAAASharedSecret=_ColubrisAAASharedSecret_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,5),_ColubrisAAASharedSecret_Type())
colubrisAAASharedSecret.setMaxAccess(_F)
if mibBuilder.loadTexts:colubrisAAASharedSecret.setStatus(_A)
class _ColubrisAAAAuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ColubrisAAAAuthenticationPort_Type.__name__=_D
_ColubrisAAAAuthenticationPort_Object=MibTableColumn
colubrisAAAAuthenticationPort=_ColubrisAAAAuthenticationPort_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,6),_ColubrisAAAAuthenticationPort_Type())
colubrisAAAAuthenticationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAAAuthenticationPort.setStatus(_A)
class _ColubrisAAAAccountingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ColubrisAAAAccountingPort_Type.__name__=_D
_ColubrisAAAAccountingPort_Object=MibTableColumn
colubrisAAAAccountingPort=_ColubrisAAAAccountingPort_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,7),_ColubrisAAAAccountingPort_Type())
colubrisAAAAccountingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAAAccountingPort.setStatus(_A)
class _ColubrisAAATimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_ColubrisAAATimeout_Type.__name__=_D
_ColubrisAAATimeout_Object=MibTableColumn
colubrisAAATimeout=_ColubrisAAATimeout_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,8),_ColubrisAAATimeout_Type())
colubrisAAATimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAATimeout.setStatus(_A)
if mibBuilder.loadTexts:colubrisAAATimeout.setUnits('seconds')
class _ColubrisAAANASId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_ColubrisAAANASId_Type.__name__=_E
_ColubrisAAANASId_Object=MibTableColumn
colubrisAAANASId=_ColubrisAAANASId_Object((1,3,6,1,4,1,8744,5,5,1,2,1,1,9),_ColubrisAAANASId_Type())
colubrisAAANASId.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisAAANASId.setStatus(_A)
_ColubrisAAAClientMIBConformance_ObjectIdentity=ObjectIdentity
colubrisAAAClientMIBConformance=_ColubrisAAAClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,5,2))
_ColubrisAAAClientMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisAAAClientMIBCompliances=_ColubrisAAAClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,5,2,1))
_ColubrisAAAClientMIBGroups_ObjectIdentity=ObjectIdentity
colubrisAAAClientMIBGroups=_ColubrisAAAClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,5,2,2))
colubrisAAAProfileMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,5,2,2,1))
colubrisAAAProfileMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:colubrisAAAProfileMIBGroup.setStatus(_A)
colubrisAAAClientMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,5,2,2,2))
colubrisAAAClientMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:colubrisAAAClientMIBGroup.setStatus(_A)
colubrisAAAClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,5,2,1,1))
colubrisAAAClientMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:colubrisAAAClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisAAAClientMIB':colubrisAAAClientMIB,'colubrisAAAClientObjects':colubrisAAAClientObjects,'colubrisAAAProfileGroup':colubrisAAAProfileGroup,'colubrisAAAProfileTable':colubrisAAAProfileTable,'colubrisAAAProfileEntry':colubrisAAAProfileEntry,_G:colubrisAAAProfileIndex,_J:colubrisAAAProfileName,_K:colubrisAAAProfilePrimaryServerIndex,_L:colubrisAAAProfileSecondaryServerIndex,'colubrisAAAServerGroup':colubrisAAAServerGroup,'colubrisAAAServerTable':colubrisAAAServerTable,'colubrisAAAServerEntry':colubrisAAAServerEntry,_I:colubrisAAAServerIndex,_M:colubrisAAAAuthenProtocol,_N:colubrisAAAAuthenMethod,_O:colubrisAAAServerName,_P:colubrisAAASharedSecret,_Q:colubrisAAAAuthenticationPort,_R:colubrisAAAAccountingPort,_S:colubrisAAATimeout,_T:colubrisAAANASId,'colubrisAAAClientMIBConformance':colubrisAAAClientMIBConformance,'colubrisAAAClientMIBCompliances':colubrisAAAClientMIBCompliances,'colubrisAAAClientMIBCompliance':colubrisAAAClientMIBCompliance,'colubrisAAAClientMIBGroups':colubrisAAAClientMIBGroups,_U:colubrisAAAProfileMIBGroup,_V:colubrisAAAClientMIBGroup})