_V='alvarionAAAClientMIBGroup'
_U='alvarionAAAProfileMIBGroup'
_T='alvarionAAANASId'
_S='alvarionAAATimeout'
_R='alvarionAAAAccountingPort'
_Q='alvarionAAAAuthenticationPort'
_P='alvarionAAASharedSecret'
_O='alvarionAAAServerName'
_N='alvarionAAAAuthenMethod'
_M='alvarionAAAAuthenProtocol'
_L='alvarionAAAProfileSecondaryServerIndex'
_K='alvarionAAAProfilePrimaryServerIndex'
_J='alvarionAAAProfileName'
_I='alvarionAAAServerIndex'
_H='not-accessible'
_G='alvarionAAAProfileIndex'
_F='read-write'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='ALVARION-AAA-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionProfileIndex,AlvarionServerIndex,AlvarionServerIndexOrZero=mibBuilder.importSymbols('ALVARION-TC','AlvarionProfileIndex','AlvarionServerIndex','AlvarionServerIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alvarionAAAClientMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,5))
_AlvarionAAAClientObjects_ObjectIdentity=ObjectIdentity
alvarionAAAClientObjects=_AlvarionAAAClientObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,5,1))
_AlvarionAAAProfileGroup_ObjectIdentity=ObjectIdentity
alvarionAAAProfileGroup=_AlvarionAAAProfileGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,5,1,1))
_AlvarionAAAProfileTable_Object=MibTable
alvarionAAAProfileTable=_AlvarionAAAProfileTable_Object((1,3,6,1,4,1,12394,1,10,5,5,1,1,1))
if mibBuilder.loadTexts:alvarionAAAProfileTable.setStatus(_A)
_AlvarionAAAProfileEntry_Object=MibTableRow
alvarionAAAProfileEntry=_AlvarionAAAProfileEntry_Object((1,3,6,1,4,1,12394,1,10,5,5,1,1,1,1))
alvarionAAAProfileEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:alvarionAAAProfileEntry.setStatus(_A)
_AlvarionAAAProfileIndex_Type=AlvarionProfileIndex
_AlvarionAAAProfileIndex_Object=MibTableColumn
alvarionAAAProfileIndex=_AlvarionAAAProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,5,1,1,1,1,1),_AlvarionAAAProfileIndex_Type())
alvarionAAAProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alvarionAAAProfileIndex.setStatus(_A)
_AlvarionAAAProfileName_Type=DisplayString
_AlvarionAAAProfileName_Object=MibTableColumn
alvarionAAAProfileName=_AlvarionAAAProfileName_Object((1,3,6,1,4,1,12394,1,10,5,5,1,1,1,1,2),_AlvarionAAAProfileName_Type())
alvarionAAAProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:alvarionAAAProfileName.setStatus(_A)
_AlvarionAAAProfilePrimaryServerIndex_Type=AlvarionServerIndexOrZero
_AlvarionAAAProfilePrimaryServerIndex_Object=MibTableColumn
alvarionAAAProfilePrimaryServerIndex=_AlvarionAAAProfilePrimaryServerIndex_Object((1,3,6,1,4,1,12394,1,10,5,5,1,1,1,1,3),_AlvarionAAAProfilePrimaryServerIndex_Type())
alvarionAAAProfilePrimaryServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAAProfilePrimaryServerIndex.setStatus(_A)
_AlvarionAAAProfileSecondaryServerIndex_Type=AlvarionServerIndexOrZero
_AlvarionAAAProfileSecondaryServerIndex_Object=MibTableColumn
alvarionAAAProfileSecondaryServerIndex=_AlvarionAAAProfileSecondaryServerIndex_Object((1,3,6,1,4,1,12394,1,10,5,5,1,1,1,1,4),_AlvarionAAAProfileSecondaryServerIndex_Type())
alvarionAAAProfileSecondaryServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAAProfileSecondaryServerIndex.setStatus(_A)
_AlvarionAAAServerGroup_ObjectIdentity=ObjectIdentity
alvarionAAAServerGroup=_AlvarionAAAServerGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,5,1,2))
_AlvarionAAAServerTable_Object=MibTable
alvarionAAAServerTable=_AlvarionAAAServerTable_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1))
if mibBuilder.loadTexts:alvarionAAAServerTable.setStatus(_A)
_AlvarionAAAServerEntry_Object=MibTableRow
alvarionAAAServerEntry=_AlvarionAAAServerEntry_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1))
alvarionAAAServerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:alvarionAAAServerEntry.setStatus(_A)
_AlvarionAAAServerIndex_Type=AlvarionServerIndex
_AlvarionAAAServerIndex_Object=MibTableColumn
alvarionAAAServerIndex=_AlvarionAAAServerIndex_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,1),_AlvarionAAAServerIndex_Type())
alvarionAAAServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alvarionAAAServerIndex.setStatus(_A)
class _AlvarionAAAAuthenProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('radius',1))
_AlvarionAAAAuthenProtocol_Type.__name__=_D
_AlvarionAAAAuthenProtocol_Object=MibTableColumn
alvarionAAAAuthenProtocol=_AlvarionAAAAuthenProtocol_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,2),_AlvarionAAAAuthenProtocol_Type())
alvarionAAAAuthenProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAAAuthenProtocol.setStatus(_A)
class _AlvarionAAAAuthenMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pap',1),('chap',2),('mschap',3),('mschapv2',4),('eapMd5',5)))
_AlvarionAAAAuthenMethod_Type.__name__=_D
_AlvarionAAAAuthenMethod_Object=MibTableColumn
alvarionAAAAuthenMethod=_AlvarionAAAAuthenMethod_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,3),_AlvarionAAAAuthenMethod_Type())
alvarionAAAAuthenMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAAAuthenMethod.setStatus(_A)
class _AlvarionAAAServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AlvarionAAAServerName_Type.__name__=_E
_AlvarionAAAServerName_Object=MibTableColumn
alvarionAAAServerName=_AlvarionAAAServerName_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,4),_AlvarionAAAServerName_Type())
alvarionAAAServerName.setMaxAccess(_F)
if mibBuilder.loadTexts:alvarionAAAServerName.setStatus(_A)
_AlvarionAAASharedSecret_Type=DisplayString
_AlvarionAAASharedSecret_Object=MibTableColumn
alvarionAAASharedSecret=_AlvarionAAASharedSecret_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,5),_AlvarionAAASharedSecret_Type())
alvarionAAASharedSecret.setMaxAccess(_F)
if mibBuilder.loadTexts:alvarionAAASharedSecret.setStatus(_A)
class _AlvarionAAAAuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlvarionAAAAuthenticationPort_Type.__name__=_D
_AlvarionAAAAuthenticationPort_Object=MibTableColumn
alvarionAAAAuthenticationPort=_AlvarionAAAAuthenticationPort_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,6),_AlvarionAAAAuthenticationPort_Type())
alvarionAAAAuthenticationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAAAuthenticationPort.setStatus(_A)
class _AlvarionAAAAccountingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlvarionAAAAccountingPort_Type.__name__=_D
_AlvarionAAAAccountingPort_Object=MibTableColumn
alvarionAAAAccountingPort=_AlvarionAAAAccountingPort_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,7),_AlvarionAAAAccountingPort_Type())
alvarionAAAAccountingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAAAccountingPort.setStatus(_A)
class _AlvarionAAATimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_AlvarionAAATimeout_Type.__name__=_D
_AlvarionAAATimeout_Object=MibTableColumn
alvarionAAATimeout=_AlvarionAAATimeout_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,8),_AlvarionAAATimeout_Type())
alvarionAAATimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAATimeout.setStatus(_A)
if mibBuilder.loadTexts:alvarionAAATimeout.setUnits('seconds')
class _AlvarionAAANASId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_AlvarionAAANASId_Type.__name__=_E
_AlvarionAAANASId_Object=MibTableColumn
alvarionAAANASId=_AlvarionAAANASId_Object((1,3,6,1,4,1,12394,1,10,5,5,1,2,1,1,9),_AlvarionAAANASId_Type())
alvarionAAANASId.setMaxAccess(_C)
if mibBuilder.loadTexts:alvarionAAANASId.setStatus(_A)
_AlvarionAAAClientMIBConformance_ObjectIdentity=ObjectIdentity
alvarionAAAClientMIBConformance=_AlvarionAAAClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,5,2))
_AlvarionAAAClientMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionAAAClientMIBCompliances=_AlvarionAAAClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,5,2,1))
_AlvarionAAAClientMIBGroups_ObjectIdentity=ObjectIdentity
alvarionAAAClientMIBGroups=_AlvarionAAAClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,5,2,2))
alvarionAAAProfileMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,5,2,2,1))
alvarionAAAProfileMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alvarionAAAProfileMIBGroup.setStatus(_A)
alvarionAAAClientMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,5,2,2,2))
alvarionAAAClientMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:alvarionAAAClientMIBGroup.setStatus(_A)
alvarionAAAClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,5,2,1,1))
alvarionAAAClientMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:alvarionAAAClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionAAAClientMIB':alvarionAAAClientMIB,'alvarionAAAClientObjects':alvarionAAAClientObjects,'alvarionAAAProfileGroup':alvarionAAAProfileGroup,'alvarionAAAProfileTable':alvarionAAAProfileTable,'alvarionAAAProfileEntry':alvarionAAAProfileEntry,_G:alvarionAAAProfileIndex,_J:alvarionAAAProfileName,_K:alvarionAAAProfilePrimaryServerIndex,_L:alvarionAAAProfileSecondaryServerIndex,'alvarionAAAServerGroup':alvarionAAAServerGroup,'alvarionAAAServerTable':alvarionAAAServerTable,'alvarionAAAServerEntry':alvarionAAAServerEntry,_I:alvarionAAAServerIndex,_M:alvarionAAAAuthenProtocol,_N:alvarionAAAAuthenMethod,_O:alvarionAAAServerName,_P:alvarionAAASharedSecret,_Q:alvarionAAAAuthenticationPort,_R:alvarionAAAAccountingPort,_S:alvarionAAATimeout,_T:alvarionAAANASId,'alvarionAAAClientMIBConformance':alvarionAAAClientMIBConformance,'alvarionAAAClientMIBCompliances':alvarionAAAClientMIBCompliances,'alvarionAAAClientMIBCompliance':alvarionAAAClientMIBCompliance,'alvarionAAAClientMIBGroups':alvarionAAAClientMIBGroups,_U:alvarionAAAProfileMIBGroup,_V:alvarionAAAClientMIBGroup})