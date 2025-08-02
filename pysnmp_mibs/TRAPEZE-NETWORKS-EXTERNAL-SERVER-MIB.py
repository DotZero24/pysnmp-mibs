_K='trpzExternalServerDnsServerGroup'
_J='trpzExtServerSecondaryDnsIpAddress'
_I='trpzExtServerPrimaryDnsIpAddress'
_H='trpzExtServerSyslogEnable'
_G='trpzExtServerSyslogPort'
_F='trpzExtServerSyslogAddress'
_E='trpzExtServerSyslogIndex'
_D='trpzExternalServerConfigGroup'
_C='read-only'
_B='TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
TrpzIpPort,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-BASIC-TC','TrpzIpPort')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzExternalServerMib=ModuleIdentity((1,3,6,1,4,1,14525,4,7))
if mibBuilder.loadTexts:trpzExternalServerMib.setRevisions(('2011-06-22 00:40','2009-10-02 00:21','2008-10-24 00:10','2006-07-31 00:04'))
class TrpzSyslogServerEnable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_TrpzExternalServerObjects_ObjectIdentity=ObjectIdentity
trpzExternalServerObjects=_TrpzExternalServerObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,7,1))
_TrpzExternalServerDataObjects_ObjectIdentity=ObjectIdentity
trpzExternalServerDataObjects=_TrpzExternalServerDataObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,7,1,1))
_TrpzExtServerSyslogTable_Object=MibTable
trpzExtServerSyslogTable=_TrpzExtServerSyslogTable_Object((1,3,6,1,4,1,14525,4,7,1,1,1))
if mibBuilder.loadTexts:trpzExtServerSyslogTable.setStatus(_A)
_TrpzExtServerSyslogEntry_Object=MibTableRow
trpzExtServerSyslogEntry=_TrpzExtServerSyslogEntry_Object((1,3,6,1,4,1,14525,4,7,1,1,1,1))
trpzExtServerSyslogEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:trpzExtServerSyslogEntry.setStatus(_A)
_TrpzExtServerSyslogIndex_Type=Unsigned32
_TrpzExtServerSyslogIndex_Object=MibTableColumn
trpzExtServerSyslogIndex=_TrpzExtServerSyslogIndex_Object((1,3,6,1,4,1,14525,4,7,1,1,1,1,1),_TrpzExtServerSyslogIndex_Type())
trpzExtServerSyslogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzExtServerSyslogIndex.setStatus(_A)
_TrpzExtServerSyslogAddress_Type=IpAddress
_TrpzExtServerSyslogAddress_Object=MibTableColumn
trpzExtServerSyslogAddress=_TrpzExtServerSyslogAddress_Object((1,3,6,1,4,1,14525,4,7,1,1,1,1,2),_TrpzExtServerSyslogAddress_Type())
trpzExtServerSyslogAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzExtServerSyslogAddress.setStatus(_A)
_TrpzExtServerSyslogPort_Type=TrpzIpPort
_TrpzExtServerSyslogPort_Object=MibTableColumn
trpzExtServerSyslogPort=_TrpzExtServerSyslogPort_Object((1,3,6,1,4,1,14525,4,7,1,1,1,1,3),_TrpzExtServerSyslogPort_Type())
trpzExtServerSyslogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzExtServerSyslogPort.setStatus(_A)
_TrpzExtServerSyslogEnable_Type=TrpzSyslogServerEnable
_TrpzExtServerSyslogEnable_Object=MibTableColumn
trpzExtServerSyslogEnable=_TrpzExtServerSyslogEnable_Object((1,3,6,1,4,1,14525,4,7,1,1,1,1,4),_TrpzExtServerSyslogEnable_Type())
trpzExtServerSyslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzExtServerSyslogEnable.setStatus(_A)
_TrpzExternalServerGlobalObjects_ObjectIdentity=ObjectIdentity
trpzExternalServerGlobalObjects=_TrpzExternalServerGlobalObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,7,1,1,2))
_TrpzExtServerPrimaryDnsIpAddress_Type=IpAddress
_TrpzExtServerPrimaryDnsIpAddress_Object=MibScalar
trpzExtServerPrimaryDnsIpAddress=_TrpzExtServerPrimaryDnsIpAddress_Object((1,3,6,1,4,1,14525,4,7,1,1,2,1),_TrpzExtServerPrimaryDnsIpAddress_Type())
trpzExtServerPrimaryDnsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzExtServerPrimaryDnsIpAddress.setStatus(_A)
_TrpzExtServerSecondaryDnsIpAddress_Type=IpAddress
_TrpzExtServerSecondaryDnsIpAddress_Object=MibScalar
trpzExtServerSecondaryDnsIpAddress=_TrpzExtServerSecondaryDnsIpAddress_Object((1,3,6,1,4,1,14525,4,7,1,1,2,2),_TrpzExtServerSecondaryDnsIpAddress_Type())
trpzExtServerSecondaryDnsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzExtServerSecondaryDnsIpAddress.setStatus(_A)
_TrpzExternalServerConformance_ObjectIdentity=ObjectIdentity
trpzExternalServerConformance=_TrpzExternalServerConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,7,1,2))
_TrpzExternalServerCompliances_ObjectIdentity=ObjectIdentity
trpzExternalServerCompliances=_TrpzExternalServerCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,7,1,2,1))
_TrpzExternalServerGroups_ObjectIdentity=ObjectIdentity
trpzExternalServerGroups=_TrpzExternalServerGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,7,1,2,2))
trpzExternalServerConfigGroup=ObjectGroup((1,3,6,1,4,1,14525,4,7,1,2,2,1))
trpzExternalServerConfigGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:trpzExternalServerConfigGroup.setStatus(_A)
trpzExternalServerDnsServerGroup=ObjectGroup((1,3,6,1,4,1,14525,4,7,1,2,2,2))
trpzExternalServerDnsServerGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:trpzExternalServerDnsServerGroup.setStatus(_A)
trpzExternalServerCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,7,1,2,1,1))
trpzExternalServerCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:trpzExternalServerCompliance.setStatus('obsolete')
trpzExternalServerComplianceRev2=ModuleCompliance((1,3,6,1,4,1,14525,4,7,1,2,1,2))
trpzExternalServerComplianceRev2.setObjects(*((_B,_D),(_B,_K)))
if mibBuilder.loadTexts:trpzExternalServerComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TrpzSyslogServerEnable':TrpzSyslogServerEnable,'trpzExternalServerMib':trpzExternalServerMib,'trpzExternalServerObjects':trpzExternalServerObjects,'trpzExternalServerDataObjects':trpzExternalServerDataObjects,'trpzExtServerSyslogTable':trpzExtServerSyslogTable,'trpzExtServerSyslogEntry':trpzExtServerSyslogEntry,_E:trpzExtServerSyslogIndex,_F:trpzExtServerSyslogAddress,_G:trpzExtServerSyslogPort,_H:trpzExtServerSyslogEnable,'trpzExternalServerGlobalObjects':trpzExternalServerGlobalObjects,_I:trpzExtServerPrimaryDnsIpAddress,_J:trpzExtServerSecondaryDnsIpAddress,'trpzExternalServerConformance':trpzExternalServerConformance,'trpzExternalServerCompliances':trpzExternalServerCompliances,'trpzExternalServerCompliance':trpzExternalServerCompliance,'trpzExternalServerComplianceRev2':trpzExternalServerComplianceRev2,'trpzExternalServerGroups':trpzExternalServerGroups,_D:trpzExternalServerConfigGroup,_K:trpzExternalServerDnsServerGroup})