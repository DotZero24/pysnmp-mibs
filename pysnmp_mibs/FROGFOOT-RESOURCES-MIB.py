_Z='loadValue'
_Y='loadDescr'
_X='loadNumber'
_W='diskFree'
_V='diskTotal'
_U='diskFSType'
_T='diskDir'
_S='diskDev'
_R='diskNumber'
_Q='swapFree'
_P='swapTotal'
_O='memCache'
_N='memBuffer'
_M='memFree'
_L='memTotal'
_K='loadIndex'
_J='not-accessible'
_I='diskIndex'
_H='Integer32'
_G='resLoadGroup'
_F='resDiskGroup'
_E='resSwapGroup'
_D='resMemGroup'
_C='read-only'
_B='FROGFOOT-RESOURCES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
resources=ModuleIdentity((1,3,6,1,4,1,10002,1,1,1))
class TableIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Frogfoot_ObjectIdentity=ObjectIdentity
frogfoot=_Frogfoot_ObjectIdentity((1,3,6,1,4,1,10002))
_Servers_ObjectIdentity=ObjectIdentity
servers=_Servers_ObjectIdentity((1,3,6,1,4,1,10002,1))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,10002,1,1))
_Memory_ObjectIdentity=ObjectIdentity
memory=_Memory_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,1))
_MemTotal_Type=Gauge32
_MemTotal_Object=MibScalar
memTotal=_MemTotal_Object((1,3,6,1,4,1,10002,1,1,1,1,1),_MemTotal_Type())
memTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:memTotal.setStatus(_A)
_MemFree_Type=Gauge32
_MemFree_Object=MibScalar
memFree=_MemFree_Object((1,3,6,1,4,1,10002,1,1,1,1,2),_MemFree_Type())
memFree.setMaxAccess(_C)
if mibBuilder.loadTexts:memFree.setStatus(_A)
_MemBuffer_Type=Gauge32
_MemBuffer_Object=MibScalar
memBuffer=_MemBuffer_Object((1,3,6,1,4,1,10002,1,1,1,1,3),_MemBuffer_Type())
memBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:memBuffer.setStatus(_A)
_MemCache_Type=Gauge32
_MemCache_Object=MibScalar
memCache=_MemCache_Object((1,3,6,1,4,1,10002,1,1,1,1,4),_MemCache_Type())
memCache.setMaxAccess(_C)
if mibBuilder.loadTexts:memCache.setStatus(_A)
_Swap_ObjectIdentity=ObjectIdentity
swap=_Swap_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,2))
_SwapTotal_Type=Gauge32
_SwapTotal_Object=MibScalar
swapTotal=_SwapTotal_Object((1,3,6,1,4,1,10002,1,1,1,2,1),_SwapTotal_Type())
swapTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:swapTotal.setStatus(_A)
_SwapFree_Type=Gauge32
_SwapFree_Object=MibScalar
swapFree=_SwapFree_Object((1,3,6,1,4,1,10002,1,1,1,2,2),_SwapFree_Type())
swapFree.setMaxAccess(_C)
if mibBuilder.loadTexts:swapFree.setStatus(_A)
_Storage_ObjectIdentity=ObjectIdentity
storage=_Storage_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,3))
_DiskNumber_Type=Integer32
_DiskNumber_Object=MibScalar
diskNumber=_DiskNumber_Object((1,3,6,1,4,1,10002,1,1,1,3,1),_DiskNumber_Type())
diskNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:diskNumber.setStatus(_A)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,10002,1,1,1,3,2))
if mibBuilder.loadTexts:diskTable.setStatus(_A)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1))
diskEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:diskEntry.setStatus(_A)
_DiskIndex_Type=TableIndex
_DiskIndex_Object=MibTableColumn
diskIndex=_DiskIndex_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1,1),_DiskIndex_Type())
diskIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:diskIndex.setStatus(_A)
_DiskDev_Type=DisplayString
_DiskDev_Object=MibTableColumn
diskDev=_DiskDev_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1,2),_DiskDev_Type())
diskDev.setMaxAccess(_C)
if mibBuilder.loadTexts:diskDev.setStatus(_A)
_DiskDir_Type=DisplayString
_DiskDir_Object=MibTableColumn
diskDir=_DiskDir_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1,3),_DiskDir_Type())
diskDir.setMaxAccess(_C)
if mibBuilder.loadTexts:diskDir.setStatus(_A)
class _DiskFSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('unknown',0),('adfs',1),('affs',2),('coda',3),('cramfs',4),('ext2',5),('hpfs',6),('iso9660',7),('jffs2',8),('jfs',9),('minix',10),('msdos',11),('ncpfs',12),('nfs',13),('ntfs',14),('qnx4',15),('reiserfs',16),('romfs',17),('smbfs',18),('sysv',19),('tmpfs',20),('udf',21),('ufs',22),('vxfs',23),('xfs',24)))
_DiskFSType_Type.__name__=_H
_DiskFSType_Object=MibTableColumn
diskFSType=_DiskFSType_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1,4),_DiskFSType_Type())
diskFSType.setMaxAccess(_C)
if mibBuilder.loadTexts:diskFSType.setStatus(_A)
_DiskTotal_Type=Gauge32
_DiskTotal_Object=MibTableColumn
diskTotal=_DiskTotal_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1,5),_DiskTotal_Type())
diskTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:diskTotal.setStatus(_A)
_DiskFree_Type=Gauge32
_DiskFree_Object=MibTableColumn
diskFree=_DiskFree_Object((1,3,6,1,4,1,10002,1,1,1,3,2,1,6),_DiskFree_Type())
diskFree.setMaxAccess(_C)
if mibBuilder.loadTexts:diskFree.setStatus(_A)
_Load_ObjectIdentity=ObjectIdentity
load=_Load_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,4))
_LoadNumber_Type=Integer32
_LoadNumber_Object=MibScalar
loadNumber=_LoadNumber_Object((1,3,6,1,4,1,10002,1,1,1,4,1),_LoadNumber_Type())
loadNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:loadNumber.setStatus(_A)
_LoadTable_Object=MibTable
loadTable=_LoadTable_Object((1,3,6,1,4,1,10002,1,1,1,4,2))
if mibBuilder.loadTexts:loadTable.setStatus(_A)
_LoadEntry_Object=MibTableRow
loadEntry=_LoadEntry_Object((1,3,6,1,4,1,10002,1,1,1,4,2,1))
loadEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:loadEntry.setStatus(_A)
_LoadIndex_Type=TableIndex
_LoadIndex_Object=MibTableColumn
loadIndex=_LoadIndex_Object((1,3,6,1,4,1,10002,1,1,1,4,2,1,1),_LoadIndex_Type())
loadIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:loadIndex.setStatus(_A)
_LoadDescr_Type=DisplayString
_LoadDescr_Object=MibTableColumn
loadDescr=_LoadDescr_Object((1,3,6,1,4,1,10002,1,1,1,4,2,1,2),_LoadDescr_Type())
loadDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:loadDescr.setStatus(_A)
_LoadValue_Type=Gauge32
_LoadValue_Object=MibTableColumn
loadValue=_LoadValue_Object((1,3,6,1,4,1,10002,1,1,1,4,2,1,3),_LoadValue_Type())
loadValue.setMaxAccess(_C)
if mibBuilder.loadTexts:loadValue.setStatus(_A)
_ResMIB_ObjectIdentity=ObjectIdentity
resMIB=_ResMIB_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,31))
_ResMIBObjects_ObjectIdentity=ObjectIdentity
resMIBObjects=_ResMIBObjects_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,31,1))
_ResConformance_ObjectIdentity=ObjectIdentity
resConformance=_ResConformance_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,31,2))
_ResGroups_ObjectIdentity=ObjectIdentity
resGroups=_ResGroups_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,31,2,1))
_ResCompliances_ObjectIdentity=ObjectIdentity
resCompliances=_ResCompliances_ObjectIdentity((1,3,6,1,4,1,10002,1,1,1,31,2,2))
resMemGroup=ObjectGroup((1,3,6,1,4,1,10002,1,1,1,31,2,1,1))
resMemGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:resMemGroup.setStatus(_A)
resSwapGroup=ObjectGroup((1,3,6,1,4,1,10002,1,1,1,31,2,1,2))
resSwapGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:resSwapGroup.setStatus(_A)
resDiskGroup=ObjectGroup((1,3,6,1,4,1,10002,1,1,1,31,2,1,3))
resDiskGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:resDiskGroup.setStatus(_A)
resLoadGroup=ObjectGroup((1,3,6,1,4,1,10002,1,1,1,31,2,1,4))
resLoadGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:resLoadGroup.setStatus(_A)
resCompliance=ModuleCompliance((1,3,6,1,4,1,10002,1,1,1,31,2,2,1))
resCompliance.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:resCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TableIndex':TableIndex,'frogfoot':frogfoot,'servers':servers,'system':system,'resources':resources,'memory':memory,_L:memTotal,_M:memFree,_N:memBuffer,_O:memCache,'swap':swap,_P:swapTotal,_Q:swapFree,'storage':storage,_R:diskNumber,'diskTable':diskTable,'diskEntry':diskEntry,_I:diskIndex,_S:diskDev,_T:diskDir,_U:diskFSType,_V:diskTotal,_W:diskFree,'load':load,_X:loadNumber,'loadTable':loadTable,'loadEntry':loadEntry,_K:loadIndex,_Y:loadDescr,_Z:loadValue,'resMIB':resMIB,'resMIBObjects':resMIBObjects,'resConformance':resConformance,'resGroups':resGroups,_D:resMemGroup,_E:resSwapGroup,_F:resDiskGroup,_G:resLoadGroup,'resCompliances':resCompliances,'resCompliance':resCompliance})