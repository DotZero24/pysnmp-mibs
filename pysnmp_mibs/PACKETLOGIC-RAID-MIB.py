_G='diskEntryIndex'
_F='not-accessible'
_E='ldEntryIndex'
_D='PACKETLOGIC-RAID-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
hw,=mibBuilder.importSymbols('PACKETLOGIC-HW-MIB','hw')
packetlogic2,=mibBuilder.importSymbols('PACKETLOGIC-MIB','packetlogic2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
raid=ModuleIdentity((1,3,6,1,4,1,15397,2,30,1))
if mibBuilder.loadTexts:raid.setRevisions(('2012-12-13 13:22',))
_RaidCfg_ObjectIdentity=ObjectIdentity
raidCfg=_RaidCfg_ObjectIdentity((1,3,6,1,4,1,15397,2,30,1,1))
_AdpNumber_Type=Unsigned32
_AdpNumber_Object=MibScalar
adpNumber=_AdpNumber_Object((1,3,6,1,4,1,15397,2,30,1,1,1),_AdpNumber_Type())
adpNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adpNumber.setStatus(_A)
_LdNumber_Type=Unsigned32
_LdNumber_Object=MibScalar
ldNumber=_LdNumber_Object((1,3,6,1,4,1,15397,2,30,1,1,2),_LdNumber_Type())
ldNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ldNumber.setStatus(_A)
_DiskNumber_Type=Unsigned32
_DiskNumber_Object=MibScalar
diskNumber=_DiskNumber_Object((1,3,6,1,4,1,15397,2,30,1,1,3),_DiskNumber_Type())
diskNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:diskNumber.setStatus(_A)
_Ld_Object=MibTable
ld=_Ld_Object((1,3,6,1,4,1,15397,2,30,1,3))
if mibBuilder.loadTexts:ld.setStatus(_A)
_LdEntry_Object=MibTableRow
ldEntry=_LdEntry_Object((1,3,6,1,4,1,15397,2,30,1,3,1))
ldEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ldEntry.setStatus(_A)
_LdId_Type=DisplayString
_LdId_Object=MibTableColumn
ldId=_LdId_Object((1,3,6,1,4,1,15397,2,30,1,3,1,1),_LdId_Type())
ldId.setMaxAccess(_B)
if mibBuilder.loadTexts:ldId.setStatus(_A)
_LdState_Type=DisplayString
_LdState_Object=MibTableColumn
ldState=_LdState_Object((1,3,6,1,4,1,15397,2,30,1,3,1,2),_LdState_Type())
ldState.setMaxAccess(_B)
if mibBuilder.loadTexts:ldState.setStatus(_A)
class _LdEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LdEntryIndex_Type.__name__=_C
_LdEntryIndex_Object=MibTableColumn
ldEntryIndex=_LdEntryIndex_Object((1,3,6,1,4,1,15397,2,30,1,3,1,999),_LdEntryIndex_Type())
ldEntryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ldEntryIndex.setStatus(_A)
_Disk_Object=MibTable
disk=_Disk_Object((1,3,6,1,4,1,15397,2,30,1,4))
if mibBuilder.loadTexts:disk.setStatus(_A)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,15397,2,30,1,4,1))
diskEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:diskEntry.setStatus(_A)
_DiskId_Type=DisplayString
_DiskId_Object=MibTableColumn
diskId=_DiskId_Object((1,3,6,1,4,1,15397,2,30,1,4,1,1),_DiskId_Type())
diskId.setMaxAccess(_B)
if mibBuilder.loadTexts:diskId.setStatus(_A)
_DiskState_Type=DisplayString
_DiskState_Object=MibTableColumn
diskState=_DiskState_Object((1,3,6,1,4,1,15397,2,30,1,4,1,2),_DiskState_Type())
diskState.setMaxAccess(_B)
if mibBuilder.loadTexts:diskState.setStatus(_A)
class _DiskEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DiskEntryIndex_Type.__name__=_C
_DiskEntryIndex_Object=MibTableColumn
diskEntryIndex=_DiskEntryIndex_Object((1,3,6,1,4,1,15397,2,30,1,4,1,999),_DiskEntryIndex_Type())
diskEntryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:diskEntryIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'raid':raid,'raidCfg':raidCfg,'adpNumber':adpNumber,'ldNumber':ldNumber,'diskNumber':diskNumber,'ld':ld,'ldEntry':ldEntry,'ldId':ldId,'ldState':ldState,_E:ldEntryIndex,'disk':disk,'diskEntry':diskEntry,'diskId':diskId,'diskState':diskState,_G:diskEntryIndex})