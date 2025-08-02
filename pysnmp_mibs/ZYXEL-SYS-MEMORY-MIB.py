_F='zySysMemoryPoolId'
_E='ZYXEL-SYS-MEMORY-MIB'
_D='Unsigned32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelSysMemory=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,50))
_ZyxelSysMemoryPoolStatus_ObjectIdentity=ObjectIdentity
zyxelSysMemoryPoolStatus=_ZyxelSysMemoryPoolStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,50,1))
_ZyxelSysMemoryPoolTable_Object=MibTable
zyxelSysMemoryPoolTable=_ZyxelSysMemoryPoolTable_Object((1,3,6,1,4,1,890,1,15,3,50,1,1))
if mibBuilder.loadTexts:zyxelSysMemoryPoolTable.setStatus(_A)
_ZyxelSysMemoryPoolEntry_Object=MibTableRow
zyxelSysMemoryPoolEntry=_ZyxelSysMemoryPoolEntry_Object((1,3,6,1,4,1,890,1,15,3,50,1,1,1))
zyxelSysMemoryPoolEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelSysMemoryPoolEntry.setStatus(_A)
_ZySysMemoryPoolId_Type=Unsigned32
_ZySysMemoryPoolId_Object=MibTableColumn
zySysMemoryPoolId=_ZySysMemoryPoolId_Object((1,3,6,1,4,1,890,1,15,3,50,1,1,1,1),_ZySysMemoryPoolId_Type())
zySysMemoryPoolId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zySysMemoryPoolId.setStatus(_A)
class _ZySysMemoryPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZySysMemoryPoolName_Type.__name__=_C
_ZySysMemoryPoolName_Object=MibTableColumn
zySysMemoryPoolName=_ZySysMemoryPoolName_Object((1,3,6,1,4,1,890,1,15,3,50,1,1,1,2),_ZySysMemoryPoolName_Type())
zySysMemoryPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMemoryPoolName.setStatus(_A)
_ZySysMemoryPoolTotalSize_Type=Unsigned32
_ZySysMemoryPoolTotalSize_Object=MibTableColumn
zySysMemoryPoolTotalSize=_ZySysMemoryPoolTotalSize_Object((1,3,6,1,4,1,890,1,15,3,50,1,1,1,3),_ZySysMemoryPoolTotalSize_Type())
zySysMemoryPoolTotalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMemoryPoolTotalSize.setStatus(_A)
_ZySysMemoryPoolUsedSize_Type=Unsigned32
_ZySysMemoryPoolUsedSize_Object=MibTableColumn
zySysMemoryPoolUsedSize=_ZySysMemoryPoolUsedSize_Object((1,3,6,1,4,1,890,1,15,3,50,1,1,1,4),_ZySysMemoryPoolUsedSize_Type())
zySysMemoryPoolUsedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMemoryPoolUsedSize.setStatus(_A)
class _ZySysMemoryPoolUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZySysMemoryPoolUtilization_Type.__name__=_D
_ZySysMemoryPoolUtilization_Object=MibTableColumn
zySysMemoryPoolUtilization=_ZySysMemoryPoolUtilization_Object((1,3,6,1,4,1,890,1,15,3,50,1,1,1,5),_ZySysMemoryPoolUtilization_Type())
zySysMemoryPoolUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMemoryPoolUtilization.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxelSysMemory':zyxelSysMemory,'zyxelSysMemoryPoolStatus':zyxelSysMemoryPoolStatus,'zyxelSysMemoryPoolTable':zyxelSysMemoryPoolTable,'zyxelSysMemoryPoolEntry':zyxelSysMemoryPoolEntry,_F:zySysMemoryPoolId,'zySysMemoryPoolName':zySysMemoryPoolName,'zySysMemoryPoolTotalSize':zySysMemoryPoolTotalSize,'zySysMemoryPoolUsedSize':zySysMemoryPoolUsedSize,'zySysMemoryPoolUtilization':zySysMemoryPoolUtilization})