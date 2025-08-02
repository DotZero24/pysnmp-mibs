_I='ipsGeneralNotificationsGroup'
_H='ipsGeneralInformationGroup'
_G='ipsPolicyInstall'
_F='ipsPolicyTime'
_E='ipsSoftwareVersion'
_D='ipsSecurityPolicy'
_C='read-only'
_B='current'
_A='STONESOFT-IPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
stonesoftIPS,stonesoftModules=mibBuilder.importSymbols('STONESOFT-SMI-MIB','stonesoftIPS','stonesoftModules')
stonesoftIPSMibModule=ModuleIdentity((1,3,6,1,4,1,1369,3,3))
if mibBuilder.loadTexts:stonesoftIPSMibModule.setRevisions(('2007-01-04 00:00',))
_IpsObjects_ObjectIdentity=ObjectIdentity
ipsObjects=_IpsObjects_ObjectIdentity((1,3,6,1,4,1,1369,5,5,1))
_IpsSoftwareVersion_Type=DisplayString
_IpsSoftwareVersion_Object=MibScalar
ipsSoftwareVersion=_IpsSoftwareVersion_Object((1,3,6,1,4,1,1369,5,5,1,1),_IpsSoftwareVersion_Type())
ipsSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsSoftwareVersion.setStatus(_B)
_IpsSecurityPolicy_Type=DisplayString
_IpsSecurityPolicy_Object=MibScalar
ipsSecurityPolicy=_IpsSecurityPolicy_Object((1,3,6,1,4,1,1369,5,5,1,2),_IpsSecurityPolicy_Type())
ipsSecurityPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsSecurityPolicy.setStatus(_B)
_IpsPolicyTime_Type=TimeStamp
_IpsPolicyTime_Object=MibScalar
ipsPolicyTime=_IpsPolicyTime_Object((1,3,6,1,4,1,1369,5,5,1,3),_IpsPolicyTime_Type())
ipsPolicyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsPolicyTime.setStatus(_B)
_IpsEvents_ObjectIdentity=ObjectIdentity
ipsEvents=_IpsEvents_ObjectIdentity((1,3,6,1,4,1,1369,5,5,2))
_IpsEventsV2_ObjectIdentity=ObjectIdentity
ipsEventsV2=_IpsEventsV2_ObjectIdentity((1,3,6,1,4,1,1369,5,5,2,0))
_IpsConformance_ObjectIdentity=ObjectIdentity
ipsConformance=_IpsConformance_ObjectIdentity((1,3,6,1,4,1,1369,5,5,3))
_IpsGroups_ObjectIdentity=ObjectIdentity
ipsGroups=_IpsGroups_ObjectIdentity((1,3,6,1,4,1,1369,5,5,3,1))
_IpsCompliances_ObjectIdentity=ObjectIdentity
ipsCompliances=_IpsCompliances_ObjectIdentity((1,3,6,1,4,1,1369,5,5,3,2))
ipsGeneralInformationGroup=ObjectGroup((1,3,6,1,4,1,1369,5,5,3,1,1))
ipsGeneralInformationGroup.setObjects(*((_A,_E),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ipsGeneralInformationGroup.setStatus(_B)
ipsPolicyInstall=NotificationType((1,3,6,1,4,1,1369,5,5,2,0,1))
ipsPolicyInstall.setObjects((_A,_D))
if mibBuilder.loadTexts:ipsPolicyInstall.setStatus(_B)
ipsGeneralNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1369,5,5,3,1,2))
ipsGeneralNotificationsGroup.setObjects((_A,_G))
if mibBuilder.loadTexts:ipsGeneralNotificationsGroup.setStatus(_B)
ipsCompliance1=ModuleCompliance((1,3,6,1,4,1,1369,5,5,3,2,1))
ipsCompliance1.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ipsCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'stonesoftIPSMibModule':stonesoftIPSMibModule,'ipsObjects':ipsObjects,_E:ipsSoftwareVersion,_D:ipsSecurityPolicy,_F:ipsPolicyTime,'ipsEvents':ipsEvents,'ipsEventsV2':ipsEventsV2,_G:ipsPolicyInstall,'ipsConformance':ipsConformance,'ipsGroups':ipsGroups,_H:ipsGeneralInformationGroup,_I:ipsGeneralNotificationsGroup,'ipsCompliances':ipsCompliances,'ipsCompliance1':ipsCompliance1})