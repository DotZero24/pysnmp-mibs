_D='eltMesIssSntpUnicastServerEntry'
_C='ELTEX-MES-ISS-SNTP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
fsSntpUnicastServerEntry,=mibBuilder.importSymbols('FSSNTP-MIB','fsSntpUnicastServerEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssSntpMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,16))
if mibBuilder.loadTexts:eltMesIssSntpMIB.setRevisions(('2019-08-15 00:00','2020-12-11 00:00'))
class NtpStratumType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltMesIssSntpObjects_ObjectIdentity=ObjectIdentity
eltMesIssSntpObjects=_EltMesIssSntpObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,16,1))
_EltMesIssSntpUnicast_ObjectIdentity=ObjectIdentity
eltMesIssSntpUnicast=_EltMesIssSntpUnicast_ObjectIdentity((1,3,6,1,4,1,35265,1,139,16,1,1))
_EltMesIssSntpUnicastServerTable_Object=MibTable
eltMesIssSntpUnicastServerTable=_EltMesIssSntpUnicastServerTable_Object((1,3,6,1,4,1,35265,1,139,16,1,1,1))
if mibBuilder.loadTexts:eltMesIssSntpUnicastServerTable.setStatus(_A)
_EltMesIssSntpUnicastServerEntry_Object=MibTableRow
eltMesIssSntpUnicastServerEntry=_EltMesIssSntpUnicastServerEntry_Object((1,3,6,1,4,1,35265,1,139,16,1,1,1,1))
if mibBuilder.loadTexts:eltMesIssSntpUnicastServerEntry.setStatus(_A)
_EltMesIssSntpUnicastServerStratum_Type=NtpStratumType
_EltMesIssSntpUnicastServerStratum_Object=MibTableColumn
eltMesIssSntpUnicastServerStratum=_EltMesIssSntpUnicastServerStratum_Object((1,3,6,1,4,1,35265,1,139,16,1,1,1,1,1),_EltMesIssSntpUnicastServerStratum_Type())
eltMesIssSntpUnicastServerStratum.setMaxAccess('read-only')
if mibBuilder.loadTexts:eltMesIssSntpUnicastServerStratum.setStatus(_A)
class _EltMesIssSntpUnicastServerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EltMesIssSntpUnicastServerPriority_Type.__name__=_B
_EltMesIssSntpUnicastServerPriority_Object=MibTableColumn
eltMesIssSntpUnicastServerPriority=_EltMesIssSntpUnicastServerPriority_Object((1,3,6,1,4,1,35265,1,139,16,1,1,1,1,2),_EltMesIssSntpUnicastServerPriority_Type())
eltMesIssSntpUnicastServerPriority.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssSntpUnicastServerPriority.setStatus(_A)
fsSntpUnicastServerEntry.registerAugmentions((_C,_D))
eltMesIssSntpUnicastServerEntry.setIndexNames(*fsSntpUnicastServerEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'NtpStratumType':NtpStratumType,'eltMesIssSntpMIB':eltMesIssSntpMIB,'eltMesIssSntpObjects':eltMesIssSntpObjects,'eltMesIssSntpUnicast':eltMesIssSntpUnicast,'eltMesIssSntpUnicastServerTable':eltMesIssSntpUnicastServerTable,_D:eltMesIssSntpUnicastServerEntry,'eltMesIssSntpUnicastServerStratum':eltMesIssSntpUnicastServerStratum,'eltMesIssSntpUnicastServerPriority':eltMesIssSntpUnicastServerPriority})