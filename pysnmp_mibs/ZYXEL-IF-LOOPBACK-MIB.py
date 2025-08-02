_D='zyIfLoopbackId'
_C='ZYXEL-IF-LOOPBACK-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIfLoopback=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,28))
_ZyxelIfLoopbackSetup_ObjectIdentity=ObjectIdentity
zyxelIfLoopbackSetup=_ZyxelIfLoopbackSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,28,1))
_ZyIfLoopbackMaxNumberOfIfs_Type=Integer32
_ZyIfLoopbackMaxNumberOfIfs_Object=MibScalar
zyIfLoopbackMaxNumberOfIfs=_ZyIfLoopbackMaxNumberOfIfs_Object((1,3,6,1,4,1,890,1,15,3,28,1,1),_ZyIfLoopbackMaxNumberOfIfs_Type())
zyIfLoopbackMaxNumberOfIfs.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyIfLoopbackMaxNumberOfIfs.setStatus(_A)
_ZyxelIfLoopbackTable_Object=MibTable
zyxelIfLoopbackTable=_ZyxelIfLoopbackTable_Object((1,3,6,1,4,1,890,1,15,3,28,1,2))
if mibBuilder.loadTexts:zyxelIfLoopbackTable.setStatus(_A)
_ZyxelIfLoopbackEntry_Object=MibTableRow
zyxelIfLoopbackEntry=_ZyxelIfLoopbackEntry_Object((1,3,6,1,4,1,890,1,15,3,28,1,2,1))
zyxelIfLoopbackEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelIfLoopbackEntry.setStatus(_A)
_ZyIfLoopbackId_Type=Integer32
_ZyIfLoopbackId_Object=MibTableColumn
zyIfLoopbackId=_ZyIfLoopbackId_Object((1,3,6,1,4,1,890,1,15,3,28,1,2,1,1),_ZyIfLoopbackId_Type())
zyIfLoopbackId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyIfLoopbackId.setStatus(_A)
_ZyIfLoopbackName_Type=OctetString
_ZyIfLoopbackName_Object=MibTableColumn
zyIfLoopbackName=_ZyIfLoopbackName_Object((1,3,6,1,4,1,890,1,15,3,28,1,2,1,2),_ZyIfLoopbackName_Type())
zyIfLoopbackName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIfLoopbackName.setStatus(_A)
_ZyIfLoopbackIpAddress_Type=IpAddress
_ZyIfLoopbackIpAddress_Object=MibTableColumn
zyIfLoopbackIpAddress=_ZyIfLoopbackIpAddress_Object((1,3,6,1,4,1,890,1,15,3,28,1,2,1,3),_ZyIfLoopbackIpAddress_Type())
zyIfLoopbackIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIfLoopbackIpAddress.setStatus(_A)
_ZyIfLoopbackMask_Type=IpAddress
_ZyIfLoopbackMask_Object=MibTableColumn
zyIfLoopbackMask=_ZyIfLoopbackMask_Object((1,3,6,1,4,1,890,1,15,3,28,1,2,1,4),_ZyIfLoopbackMask_Type())
zyIfLoopbackMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIfLoopbackMask.setStatus(_A)
_ZyIfLoopbackRowStatus_Type=RowStatus
_ZyIfLoopbackRowStatus_Object=MibTableColumn
zyIfLoopbackRowStatus=_ZyIfLoopbackRowStatus_Object((1,3,6,1,4,1,890,1,15,3,28,1,2,1,5),_ZyIfLoopbackRowStatus_Type())
zyIfLoopbackRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyIfLoopbackRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelIfLoopback':zyxelIfLoopback,'zyxelIfLoopbackSetup':zyxelIfLoopbackSetup,'zyIfLoopbackMaxNumberOfIfs':zyIfLoopbackMaxNumberOfIfs,'zyxelIfLoopbackTable':zyxelIfLoopbackTable,'zyxelIfLoopbackEntry':zyxelIfLoopbackEntry,_D:zyIfLoopbackId,'zyIfLoopbackName':zyIfLoopbackName,'zyIfLoopbackIpAddress':zyIfLoopbackIpAddress,'zyIfLoopbackMask':zyIfLoopbackMask,'zyIfLoopbackRowStatus':zyIfLoopbackRowStatus})