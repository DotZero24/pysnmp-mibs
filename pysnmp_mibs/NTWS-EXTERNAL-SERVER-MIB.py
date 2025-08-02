_H='ntwsExternalServerConfigGroup'
_G='ntwsExtServerSyslogEnable'
_F='ntwsExtServerSyslogPort'
_E='ntwsExtServerSyslogAddress'
_D='ntwsExtServerSyslogIndex'
_C='read-only'
_B='NTWS-EXTERNAL-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsIpPort,=mibBuilder.importSymbols('NTWS-BASIC-TC','NtwsIpPort')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntwsExternalServerMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,7))
if mibBuilder.loadTexts:ntwsExternalServerMib.setRevisions(('2008-10-24 00:10','2007-08-16 00:05','2006-07-31 00:04'))
class NtwsSyslogServerEnable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_NtwsExternalServerObjects_ObjectIdentity=ObjectIdentity
ntwsExternalServerObjects=_NtwsExternalServerObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,7,1))
_NtwsExternalServerDataObjects_ObjectIdentity=ObjectIdentity
ntwsExternalServerDataObjects=_NtwsExternalServerDataObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,7,1,1))
_NtwsExtServerSyslogTable_Object=MibTable
ntwsExtServerSyslogTable=_NtwsExtServerSyslogTable_Object((1,3,6,1,4,1,45,6,1,4,7,1,1,1))
if mibBuilder.loadTexts:ntwsExtServerSyslogTable.setStatus(_A)
_NtwsExtServerSyslogEntry_Object=MibTableRow
ntwsExtServerSyslogEntry=_NtwsExtServerSyslogEntry_Object((1,3,6,1,4,1,45,6,1,4,7,1,1,1,1))
ntwsExtServerSyslogEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ntwsExtServerSyslogEntry.setStatus(_A)
_NtwsExtServerSyslogIndex_Type=Unsigned32
_NtwsExtServerSyslogIndex_Object=MibTableColumn
ntwsExtServerSyslogIndex=_NtwsExtServerSyslogIndex_Object((1,3,6,1,4,1,45,6,1,4,7,1,1,1,1,1),_NtwsExtServerSyslogIndex_Type())
ntwsExtServerSyslogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntwsExtServerSyslogIndex.setStatus(_A)
_NtwsExtServerSyslogAddress_Type=IpAddress
_NtwsExtServerSyslogAddress_Object=MibTableColumn
ntwsExtServerSyslogAddress=_NtwsExtServerSyslogAddress_Object((1,3,6,1,4,1,45,6,1,4,7,1,1,1,1,2),_NtwsExtServerSyslogAddress_Type())
ntwsExtServerSyslogAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsExtServerSyslogAddress.setStatus(_A)
_NtwsExtServerSyslogPort_Type=NtwsIpPort
_NtwsExtServerSyslogPort_Object=MibTableColumn
ntwsExtServerSyslogPort=_NtwsExtServerSyslogPort_Object((1,3,6,1,4,1,45,6,1,4,7,1,1,1,1,3),_NtwsExtServerSyslogPort_Type())
ntwsExtServerSyslogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsExtServerSyslogPort.setStatus(_A)
_NtwsExtServerSyslogEnable_Type=NtwsSyslogServerEnable
_NtwsExtServerSyslogEnable_Object=MibTableColumn
ntwsExtServerSyslogEnable=_NtwsExtServerSyslogEnable_Object((1,3,6,1,4,1,45,6,1,4,7,1,1,1,1,4),_NtwsExtServerSyslogEnable_Type())
ntwsExtServerSyslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsExtServerSyslogEnable.setStatus(_A)
_NtwsExternalServerConformance_ObjectIdentity=ObjectIdentity
ntwsExternalServerConformance=_NtwsExternalServerConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,7,1,2))
_NtwsExternalServerCompliances_ObjectIdentity=ObjectIdentity
ntwsExternalServerCompliances=_NtwsExternalServerCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,7,1,2,1))
_NtwsExternalServerGroups_ObjectIdentity=ObjectIdentity
ntwsExternalServerGroups=_NtwsExternalServerGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,7,1,2,2))
ntwsExternalServerConfigGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,7,1,2,2,1))
ntwsExternalServerConfigGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ntwsExternalServerConfigGroup.setStatus(_A)
ntwsExternalServerCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,7,1,2,1,1))
ntwsExternalServerCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ntwsExternalServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NtwsSyslogServerEnable':NtwsSyslogServerEnable,'ntwsExternalServerMib':ntwsExternalServerMib,'ntwsExternalServerObjects':ntwsExternalServerObjects,'ntwsExternalServerDataObjects':ntwsExternalServerDataObjects,'ntwsExtServerSyslogTable':ntwsExtServerSyslogTable,'ntwsExtServerSyslogEntry':ntwsExtServerSyslogEntry,_D:ntwsExtServerSyslogIndex,_E:ntwsExtServerSyslogAddress,_F:ntwsExtServerSyslogPort,_G:ntwsExtServerSyslogEnable,'ntwsExternalServerConformance':ntwsExternalServerConformance,'ntwsExternalServerCompliances':ntwsExternalServerCompliances,'ntwsExternalServerCompliance':ntwsExternalServerCompliance,'ntwsExternalServerGroups':ntwsExternalServerGroups,_H:ntwsExternalServerConfigGroup})