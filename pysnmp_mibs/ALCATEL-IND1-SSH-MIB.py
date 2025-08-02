_J='alaSshConfigGroup'
_I='alaSshPubKeyEnforceAdminStatus'
_H='alaScpSftpAdminStatus'
_G='alaSshAdminStatus'
_F='disabled'
_E='enabled'
_D='read-write'
_C='ALCATEL-IND1-SSH-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Ssh,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Ssh')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1SshMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,39,1))
if mibBuilder.loadTexts:alcatelIND1SshMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1SshMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1SshMIBObjects=_AlcatelIND1SshMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,39,1,1))
if mibBuilder.loadTexts:alcatelIND1SshMIBObjects.setStatus(_A)
class _AlaSshAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaSshAdminStatus_Type.__name__=_B
_AlaSshAdminStatus_Object=MibScalar
alaSshAdminStatus=_AlaSshAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,39,1,1,1),_AlaSshAdminStatus_Type())
alaSshAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaSshAdminStatus.setStatus(_A)
class _AlaScpSftpAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaScpSftpAdminStatus_Type.__name__=_B
_AlaScpSftpAdminStatus_Object=MibScalar
alaScpSftpAdminStatus=_AlaScpSftpAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,39,1,1,2),_AlaScpSftpAdminStatus_Type())
alaScpSftpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaScpSftpAdminStatus.setStatus(_A)
class _AlaSshPubKeyEnforceAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaSshPubKeyEnforceAdminStatus_Type.__name__=_B
_AlaSshPubKeyEnforceAdminStatus_Object=MibScalar
alaSshPubKeyEnforceAdminStatus=_AlaSshPubKeyEnforceAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,39,1,1,3),_AlaSshPubKeyEnforceAdminStatus_Type())
alaSshPubKeyEnforceAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaSshPubKeyEnforceAdminStatus.setStatus(_A)
class _AlaSshPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaSshPortNumber_Type.__name__=_B
_AlaSshPortNumber_Object=MibScalar
alaSshPortNumber=_AlaSshPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,39,1,1,4),_AlaSshPortNumber_Type())
alaSshPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:alaSshPortNumber.setStatus(_A)
_AlcatelIND1SshMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1SshMIBConformance=_AlcatelIND1SshMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,39,1,2))
if mibBuilder.loadTexts:alcatelIND1SshMIBConformance.setStatus(_A)
_AlcatelIND1SshMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1SshMIBGroups=_AlcatelIND1SshMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,39,1,2,1))
if mibBuilder.loadTexts:alcatelIND1SshMIBGroups.setStatus(_A)
_AlcatelIND1SshMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1SshMIBCompliances=_AlcatelIND1SshMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,39,1,2,2))
if mibBuilder.loadTexts:alcatelIND1SshMIBCompliances.setStatus(_A)
alaSshConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,39,1,2,1,1))
alaSshConfigGroup.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:alaSshConfigGroup.setStatus(_A)
alcatelIND1SshMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,39,1,2,2,1))
alcatelIND1SshMIBCompliance.setObjects((_C,_J))
if mibBuilder.loadTexts:alcatelIND1SshMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'alcatelIND1SshMIB':alcatelIND1SshMIB,'alcatelIND1SshMIBObjects':alcatelIND1SshMIBObjects,_G:alaSshAdminStatus,_H:alaScpSftpAdminStatus,_I:alaSshPubKeyEnforceAdminStatus,'alaSshPortNumber':alaSshPortNumber,'alcatelIND1SshMIBConformance':alcatelIND1SshMIBConformance,'alcatelIND1SshMIBGroups':alcatelIND1SshMIBGroups,_J:alaSshConfigGroup,'alcatelIND1SshMIBCompliances':alcatelIND1SshMIBCompliances,'alcatelIND1SshMIBCompliance':alcatelIND1SshMIBCompliance})