if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netSnmpModuleIDs,netSnmpObjects=mibBuilder.importSymbols('NET-SNMP-MIB','netSnmpModuleIDs','netSnmpObjects')
Float,=mibBuilder.importSymbols('NET-SNMP-TC','Float')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netSnmpSystemMIB=ModuleIdentity((1,3,6,1,4,1,8072,3,1,4))
if mibBuilder.loadTexts:netSnmpSystemMIB.setRevisions(('2002-02-09 00:00',))
_NsMemory_ObjectIdentity=ObjectIdentity
nsMemory=_NsMemory_ObjectIdentity((1,3,6,1,4,1,8072,1,31))
_NsSwap_ObjectIdentity=ObjectIdentity
nsSwap=_NsSwap_ObjectIdentity((1,3,6,1,4,1,8072,1,32))
_NsCPU_ObjectIdentity=ObjectIdentity
nsCPU=_NsCPU_ObjectIdentity((1,3,6,1,4,1,8072,1,33))
_NsLoad_ObjectIdentity=ObjectIdentity
nsLoad=_NsLoad_ObjectIdentity((1,3,6,1,4,1,8072,1,34))
_NsDiskIO_ObjectIdentity=ObjectIdentity
nsDiskIO=_NsDiskIO_ObjectIdentity((1,3,6,1,4,1,8072,1,35))
mibBuilder.exportSymbols('NET-SNMP-SYSTEM-MIB',**{'nsMemory':nsMemory,'nsSwap':nsSwap,'nsCPU':nsCPU,'nsLoad':nsLoad,'nsDiskIO':nsDiskIO,'netSnmpSystemMIB':netSnmpSystemMIB})