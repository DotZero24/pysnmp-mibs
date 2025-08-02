_F='not-accessible'
_E='zyCpuProtectionReasonType'
_D='zyCpuProtectionPort'
_C='ZYXEL-CPU-PROTECTION-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelCpuProtection=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,16))
_ZyxelCpuProtectionSetup_ObjectIdentity=ObjectIdentity
zyxelCpuProtectionSetup=_ZyxelCpuProtectionSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,16,1))
_ZyxelCpuProtectionTable_Object=MibTable
zyxelCpuProtectionTable=_ZyxelCpuProtectionTable_Object((1,3,6,1,4,1,890,1,15,3,16,1,1))
if mibBuilder.loadTexts:zyxelCpuProtectionTable.setStatus(_A)
_ZyxelCpuProtectionEntry_Object=MibTableRow
zyxelCpuProtectionEntry=_ZyxelCpuProtectionEntry_Object((1,3,6,1,4,1,890,1,15,3,16,1,1,1))
zyxelCpuProtectionEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:zyxelCpuProtectionEntry.setStatus(_A)
_ZyCpuProtectionPort_Type=Integer32
_ZyCpuProtectionPort_Object=MibTableColumn
zyCpuProtectionPort=_ZyCpuProtectionPort_Object((1,3,6,1,4,1,890,1,15,3,16,1,1,1,1),_ZyCpuProtectionPort_Type())
zyCpuProtectionPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zyCpuProtectionPort.setStatus(_A)
class _ZyCpuProtectionReasonType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('arp',1),('bpdu',2),('igmp',3)))
_ZyCpuProtectionReasonType_Type.__name__=_B
_ZyCpuProtectionReasonType_Object=MibTableColumn
zyCpuProtectionReasonType=_ZyCpuProtectionReasonType_Object((1,3,6,1,4,1,890,1,15,3,16,1,1,1,2),_ZyCpuProtectionReasonType_Type())
zyCpuProtectionReasonType.setMaxAccess(_F)
if mibBuilder.loadTexts:zyCpuProtectionReasonType.setStatus(_A)
class _ZyCpuProtectionRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZyCpuProtectionRateLimit_Type.__name__=_B
_ZyCpuProtectionRateLimit_Object=MibTableColumn
zyCpuProtectionRateLimit=_ZyCpuProtectionRateLimit_Object((1,3,6,1,4,1,890,1,15,3,16,1,1,1,3),_ZyCpuProtectionRateLimit_Type())
zyCpuProtectionRateLimit.setMaxAccess('read-write')
if mibBuilder.loadTexts:zyCpuProtectionRateLimit.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelCpuProtection':zyxelCpuProtection,'zyxelCpuProtectionSetup':zyxelCpuProtectionSetup,'zyxelCpuProtectionTable':zyxelCpuProtectionTable,'zyxelCpuProtectionEntry':zyxelCpuProtectionEntry,_D:zyCpuProtectionPort,_E:zyCpuProtectionReasonType,'zyCpuProtectionRateLimit':zyCpuProtectionRateLimit})