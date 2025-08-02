_H='rbtwsExternalServerConfigGroup'
_G='rbtwsExtServerSyslogEnable'
_F='rbtwsExtServerSyslogPort'
_E='rbtwsExtServerSyslogAddress'
_D='rbtwsExtServerSyslogIndex'
_C='read-only'
_B='RBTWS-EXTERNAL-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbtwsMibs,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbtwsExternalServerMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,7))
if mibBuilder.loadTexts:rbtwsExternalServerMib.setRevisions(('2006-07-31 00:04',))
class RbtwsIpPort(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class RbtwsSyslogServerEnable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RbtwsExternalServerObjects_ObjectIdentity=ObjectIdentity
rbtwsExternalServerObjects=_RbtwsExternalServerObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,7,1))
_RbtwsExternalServerDataObjects_ObjectIdentity=ObjectIdentity
rbtwsExternalServerDataObjects=_RbtwsExternalServerDataObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,7,1,1))
_RbtwsExtServerSyslogTable_Object=MibTable
rbtwsExtServerSyslogTable=_RbtwsExtServerSyslogTable_Object((1,3,6,1,4,1,52,4,15,1,4,7,1,1,1))
if mibBuilder.loadTexts:rbtwsExtServerSyslogTable.setStatus(_A)
_RbtwsExtServerSyslogEntry_Object=MibTableRow
rbtwsExtServerSyslogEntry=_RbtwsExtServerSyslogEntry_Object((1,3,6,1,4,1,52,4,15,1,4,7,1,1,1,1))
rbtwsExtServerSyslogEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:rbtwsExtServerSyslogEntry.setStatus(_A)
_RbtwsExtServerSyslogIndex_Type=Unsigned32
_RbtwsExtServerSyslogIndex_Object=MibTableColumn
rbtwsExtServerSyslogIndex=_RbtwsExtServerSyslogIndex_Object((1,3,6,1,4,1,52,4,15,1,4,7,1,1,1,1,1),_RbtwsExtServerSyslogIndex_Type())
rbtwsExtServerSyslogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbtwsExtServerSyslogIndex.setStatus(_A)
_RbtwsExtServerSyslogAddress_Type=IpAddress
_RbtwsExtServerSyslogAddress_Object=MibTableColumn
rbtwsExtServerSyslogAddress=_RbtwsExtServerSyslogAddress_Object((1,3,6,1,4,1,52,4,15,1,4,7,1,1,1,1,2),_RbtwsExtServerSyslogAddress_Type())
rbtwsExtServerSyslogAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsExtServerSyslogAddress.setStatus(_A)
_RbtwsExtServerSyslogPort_Type=RbtwsIpPort
_RbtwsExtServerSyslogPort_Object=MibTableColumn
rbtwsExtServerSyslogPort=_RbtwsExtServerSyslogPort_Object((1,3,6,1,4,1,52,4,15,1,4,7,1,1,1,1,3),_RbtwsExtServerSyslogPort_Type())
rbtwsExtServerSyslogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsExtServerSyslogPort.setStatus(_A)
_RbtwsExtServerSyslogEnable_Type=RbtwsSyslogServerEnable
_RbtwsExtServerSyslogEnable_Object=MibTableColumn
rbtwsExtServerSyslogEnable=_RbtwsExtServerSyslogEnable_Object((1,3,6,1,4,1,52,4,15,1,4,7,1,1,1,1,4),_RbtwsExtServerSyslogEnable_Type())
rbtwsExtServerSyslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsExtServerSyslogEnable.setStatus(_A)
_RbtwsExternalServerConformance_ObjectIdentity=ObjectIdentity
rbtwsExternalServerConformance=_RbtwsExternalServerConformance_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,7,1,2))
_RbtwsExternalServerCompliances_ObjectIdentity=ObjectIdentity
rbtwsExternalServerCompliances=_RbtwsExternalServerCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,7,1,2,1))
_RbtwsExternalServerGroups_ObjectIdentity=ObjectIdentity
rbtwsExternalServerGroups=_RbtwsExternalServerGroups_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,7,1,2,2))
rbtwsExternalServerConfigGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,7,1,2,2,1))
rbtwsExternalServerConfigGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:rbtwsExternalServerConfigGroup.setStatus(_A)
rbtwsExternalServerCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,15,1,4,7,1,2,1,1))
rbtwsExternalServerCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:rbtwsExternalServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RbtwsIpPort':RbtwsIpPort,'RbtwsSyslogServerEnable':RbtwsSyslogServerEnable,'rbtwsExternalServerMib':rbtwsExternalServerMib,'rbtwsExternalServerObjects':rbtwsExternalServerObjects,'rbtwsExternalServerDataObjects':rbtwsExternalServerDataObjects,'rbtwsExtServerSyslogTable':rbtwsExtServerSyslogTable,'rbtwsExtServerSyslogEntry':rbtwsExtServerSyslogEntry,_D:rbtwsExtServerSyslogIndex,_E:rbtwsExtServerSyslogAddress,_F:rbtwsExtServerSyslogPort,_G:rbtwsExtServerSyslogEnable,'rbtwsExternalServerConformance':rbtwsExternalServerConformance,'rbtwsExternalServerCompliances':rbtwsExternalServerCompliances,'rbtwsExternalServerCompliance':rbtwsExternalServerCompliance,'rbtwsExternalServerGroups':rbtwsExternalServerGroups,_H:rbtwsExternalServerConfigGroup})