_E='snsHostIPAddr'
_D='STORMSHIELD-HOSTS-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsHosts=ModuleIdentity((1,3,6,1,4,1,11256,1,3))
if mibBuilder.loadTexts:snsHosts.setRevisions(('2017-02-20 00:00',))
_SnsHostsTable_Object=MibTable
snsHostsTable=_SnsHostsTable_Object((1,3,6,1,4,1,11256,1,3,1))
if mibBuilder.loadTexts:snsHostsTable.setStatus(_A)
_SnsHostsEntry_Object=MibTableRow
snsHostsEntry=_SnsHostsEntry_Object((1,3,6,1,4,1,11256,1,3,1,1))
snsHostsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsHostsEntry.setStatus(_A)
class _SnsHostIPAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsHostIPAddr_Type.__name__=_C
_SnsHostIPAddr_Object=MibTableColumn
snsHostIPAddr=_SnsHostIPAddr_Object((1,3,6,1,4,1,11256,1,3,1,1,1),_SnsHostIPAddr_Type())
snsHostIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHostIPAddr.setStatus(_A)
_SnsHostName_Type=SnmpAdminString
_SnsHostName_Object=MibTableColumn
snsHostName=_SnsHostName_Object((1,3,6,1,4,1,11256,1,3,1,1,2),_SnsHostName_Type())
snsHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHostName.setStatus(_A)
_SnsInterface_Type=DisplayString
_SnsInterface_Object=MibTableColumn
snsInterface=_SnsInterface_Object((1,3,6,1,4,1,11256,1,3,1,1,3),_SnsInterface_Type())
snsInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:snsInterface.setStatus(_A)
_SnsPackets_Type=Counter64
_SnsPackets_Object=MibTableColumn
snsPackets=_SnsPackets_Object((1,3,6,1,4,1,11256,1,3,1,1,4),_SnsPackets_Type())
snsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPackets.setStatus(_A)
_SnsBytes_Type=Counter64
_SnsBytes_Object=MibTableColumn
snsBytes=_SnsBytes_Object((1,3,6,1,4,1,11256,1,3,1,1,5),_SnsBytes_Type())
snsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsBytes.setStatus(_A)
_SnsCurThroughput_Type=Counter64
_SnsCurThroughput_Object=MibTableColumn
snsCurThroughput=_SnsCurThroughput_Object((1,3,6,1,4,1,11256,1,3,1,1,7),_SnsCurThroughput_Type())
snsCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsCurThroughput.setStatus(_A)
_SnsMaxThroughput_Type=Counter64
_SnsMaxThroughput_Object=MibTableColumn
snsMaxThroughput=_SnsMaxThroughput_Object((1,3,6,1,4,1,11256,1,3,1,1,8),_SnsMaxThroughput_Type())
snsMaxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsMaxThroughput.setStatus(_A)
_SnsInBytes_Type=Counter64
_SnsInBytes_Object=MibTableColumn
snsInBytes=_SnsInBytes_Object((1,3,6,1,4,1,11256,1,3,1,1,9),_SnsInBytes_Type())
snsInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsInBytes.setStatus(_A)
_SnsOutBytes_Type=Counter64
_SnsOutBytes_Object=MibTableColumn
snsOutBytes=_SnsOutBytes_Object((1,3,6,1,4,1,11256,1,3,1,1,10),_SnsOutBytes_Type())
snsOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsOutBytes.setStatus(_A)
_SnsInCurThroughput_Type=Counter64
_SnsInCurThroughput_Object=MibTableColumn
snsInCurThroughput=_SnsInCurThroughput_Object((1,3,6,1,4,1,11256,1,3,1,1,11),_SnsInCurThroughput_Type())
snsInCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsInCurThroughput.setStatus(_A)
_SnsOutCurThroughput_Type=Counter64
_SnsOutCurThroughput_Object=MibTableColumn
snsOutCurThroughput=_SnsOutCurThroughput_Object((1,3,6,1,4,1,11256,1,3,1,1,12),_SnsOutCurThroughput_Type())
snsOutCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsOutCurThroughput.setStatus(_A)
_SnsInMaxCurThroughput_Type=Counter64
_SnsInMaxCurThroughput_Object=MibTableColumn
snsInMaxCurThroughput=_SnsInMaxCurThroughput_Object((1,3,6,1,4,1,11256,1,3,1,1,13),_SnsInMaxCurThroughput_Type())
snsInMaxCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsInMaxCurThroughput.setStatus(_A)
_SnsOutMaxCurThroughput_Type=Counter64
_SnsOutMaxCurThroughput_Object=MibTableColumn
snsOutMaxCurThroughput=_SnsOutMaxCurThroughput_Object((1,3,6,1,4,1,11256,1,3,1,1,14),_SnsOutMaxCurThroughput_Type())
snsOutMaxCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsOutMaxCurThroughput.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsHosts':snsHosts,'snsHostsTable':snsHostsTable,'snsHostsEntry':snsHostsEntry,_E:snsHostIPAddr,'snsHostName':snsHostName,'snsInterface':snsInterface,'snsPackets':snsPackets,'snsBytes':snsBytes,'snsCurThroughput':snsCurThroughput,'snsMaxThroughput':snsMaxThroughput,'snsInBytes':snsInBytes,'snsOutBytes':snsOutBytes,'snsInCurThroughput':snsInCurThroughput,'snsOutCurThroughput':snsOutCurThroughput,'snsInMaxCurThroughput':snsInMaxCurThroughput,'snsOutMaxCurThroughput':snsOutMaxCurThroughput})