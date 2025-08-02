_H='not-accessible'
_G='rscResourceId'
_F='DisplayString'
_E='rscStkId'
_D='Unsigned32'
_C='AT-RESOURCE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
resource=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,21))
if mibBuilder.loadTexts:resource.setRevisions(('2008-10-20 10:00','1920-08-09 04:00'))
_RscBoardTable_Object=MibTable
rscBoardTable=_RscBoardTable_Object((1,3,6,1,4,1,207,8,4,4,3,21,1))
if mibBuilder.loadTexts:rscBoardTable.setStatus(_A)
_RscBoardEntry_Object=MibTableRow
rscBoardEntry=_RscBoardEntry_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1))
rscBoardEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:rscBoardEntry.setStatus(_A)
class _RscStkId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RscStkId_Type.__name__=_D
_RscStkId_Object=MibTableColumn
rscStkId=_RscStkId_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,1),_RscStkId_Type())
rscStkId.setMaxAccess(_H)
if mibBuilder.loadTexts:rscStkId.setStatus(_A)
class _RscResourceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967294))
_RscResourceId_Type.__name__=_D
_RscResourceId_Object=MibTableColumn
rscResourceId=_RscResourceId_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,2),_RscResourceId_Type())
rscResourceId.setMaxAccess(_H)
if mibBuilder.loadTexts:rscResourceId.setStatus(_A)
_RscBoardType_Type=DisplayString
_RscBoardType_Object=MibTableColumn
rscBoardType=_RscBoardType_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,3),_RscBoardType_Type())
rscBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:rscBoardType.setStatus(_A)
_RscBoardName_Type=DisplayString
_RscBoardName_Object=MibTableColumn
rscBoardName=_RscBoardName_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,4),_RscBoardName_Type())
rscBoardName.setMaxAccess(_B)
if mibBuilder.loadTexts:rscBoardName.setStatus(_A)
_RscBoardID_Type=Unsigned32
_RscBoardID_Object=MibTableColumn
rscBoardID=_RscBoardID_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,5),_RscBoardID_Type())
rscBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:rscBoardID.setStatus(_A)
_RscBoardBay_Type=DisplayString
_RscBoardBay_Object=MibTableColumn
rscBoardBay=_RscBoardBay_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,6),_RscBoardBay_Type())
rscBoardBay.setMaxAccess('read-write')
if mibBuilder.loadTexts:rscBoardBay.setStatus(_A)
class _RscBoardRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_RscBoardRevision_Type.__name__=_F
_RscBoardRevision_Object=MibTableColumn
rscBoardRevision=_RscBoardRevision_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,7),_RscBoardRevision_Type())
rscBoardRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:rscBoardRevision.setStatus(_A)
_RscBoardSerialNumber_Type=DisplayString
_RscBoardSerialNumber_Object=MibTableColumn
rscBoardSerialNumber=_RscBoardSerialNumber_Object((1,3,6,1,4,1,207,8,4,4,3,21,1,1,8),_RscBoardSerialNumber_Type())
rscBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rscBoardSerialNumber.setStatus(_A)
_HostInfoTable_Object=MibTable
hostInfoTable=_HostInfoTable_Object((1,3,6,1,4,1,207,8,4,4,3,21,2))
if mibBuilder.loadTexts:hostInfoTable.setStatus(_A)
_HostInfoEntry_Object=MibTableRow
hostInfoEntry=_HostInfoEntry_Object((1,3,6,1,4,1,207,8,4,4,3,21,2,1))
hostInfoEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hostInfoEntry.setStatus(_A)
_HostInfoDRAM_Type=DisplayString
_HostInfoDRAM_Object=MibTableColumn
hostInfoDRAM=_HostInfoDRAM_Object((1,3,6,1,4,1,207,8,4,4,3,21,2,1,1),_HostInfoDRAM_Type())
hostInfoDRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:hostInfoDRAM.setStatus(_A)
_HostInfoFlash_Type=DisplayString
_HostInfoFlash_Object=MibTableColumn
hostInfoFlash=_HostInfoFlash_Object((1,3,6,1,4,1,207,8,4,4,3,21,2,1,2),_HostInfoFlash_Type())
hostInfoFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:hostInfoFlash.setStatus(_A)
_HostInfoUptime_Type=DisplayString
_HostInfoUptime_Object=MibTableColumn
hostInfoUptime=_HostInfoUptime_Object((1,3,6,1,4,1,207,8,4,4,3,21,2,1,3),_HostInfoUptime_Type())
hostInfoUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:hostInfoUptime.setStatus(_A)
_HostInfoBootloaderVersion_Type=DisplayString
_HostInfoBootloaderVersion_Object=MibTableColumn
hostInfoBootloaderVersion=_HostInfoBootloaderVersion_Object((1,3,6,1,4,1,207,8,4,4,3,21,2,1,4),_HostInfoBootloaderVersion_Type())
hostInfoBootloaderVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hostInfoBootloaderVersion.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'resource':resource,'rscBoardTable':rscBoardTable,'rscBoardEntry':rscBoardEntry,_E:rscStkId,_G:rscResourceId,'rscBoardType':rscBoardType,'rscBoardName':rscBoardName,'rscBoardID':rscBoardID,'rscBoardBay':rscBoardBay,'rscBoardRevision':rscBoardRevision,'rscBoardSerialNumber':rscBoardSerialNumber,'hostInfoTable':hostInfoTable,'hostInfoEntry':hostInfoEntry,'hostInfoDRAM':hostInfoDRAM,'hostInfoFlash':hostInfoFlash,'hostInfoUptime':hostInfoUptime,'hostInfoBootloaderVersion':hostInfoBootloaderVersion})