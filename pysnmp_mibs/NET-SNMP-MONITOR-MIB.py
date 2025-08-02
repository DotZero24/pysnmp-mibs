if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netSnmpModuleIDs,netSnmpObjects=mibBuilder.importSymbols('NET-SNMP-MIB','netSnmpModuleIDs','netSnmpObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netSnmpMonitorMIB=ModuleIdentity((1,3,6,1,4,1,8072,3,1,3))
if mibBuilder.loadTexts:netSnmpMonitorMIB.setRevisions(('2002-02-09 00:00',))
_NsProcess_ObjectIdentity=ObjectIdentity
nsProcess=_NsProcess_ObjectIdentity((1,3,6,1,4,1,8072,1,21))
_NsDisk_ObjectIdentity=ObjectIdentity
nsDisk=_NsDisk_ObjectIdentity((1,3,6,1,4,1,8072,1,22))
_NsFile_ObjectIdentity=ObjectIdentity
nsFile=_NsFile_ObjectIdentity((1,3,6,1,4,1,8072,1,23))
_NsLog_ObjectIdentity=ObjectIdentity
nsLog=_NsLog_ObjectIdentity((1,3,6,1,4,1,8072,1,24))
mibBuilder.exportSymbols('NET-SNMP-MONITOR-MIB',**{'nsProcess':nsProcess,'nsDisk':nsDisk,'nsFile':nsFile,'nsLog':nsLog,'netSnmpMonitorMIB':netSnmpMonitorMIB})