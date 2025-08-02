_G='not-accessible'
_F='zyIfId'
_E='zyIfType'
_D='read-only'
_C='Integer32'
_B='ZYXEL-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIf=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,27))
_ZyxelIfSetup_ObjectIdentity=ObjectIdentity
zyxelIfSetup=_ZyxelIfSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,27,1))
_ZyIfMaxNumberOfVlanIfs_Type=Integer32
_ZyIfMaxNumberOfVlanIfs_Object=MibScalar
zyIfMaxNumberOfVlanIfs=_ZyIfMaxNumberOfVlanIfs_Object((1,3,6,1,4,1,890,1,15,3,27,1,1),_ZyIfMaxNumberOfVlanIfs_Type())
zyIfMaxNumberOfVlanIfs.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIfMaxNumberOfVlanIfs.setStatus(_A)
_ZyIfMaxNumberOfLoopbackIfs_Type=Integer32
_ZyIfMaxNumberOfLoopbackIfs_Object=MibScalar
zyIfMaxNumberOfLoopbackIfs=_ZyIfMaxNumberOfLoopbackIfs_Object((1,3,6,1,4,1,890,1,15,3,27,1,2),_ZyIfMaxNumberOfLoopbackIfs_Type())
zyIfMaxNumberOfLoopbackIfs.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIfMaxNumberOfLoopbackIfs.setStatus(_A)
_ZyxelIfTable_Object=MibTable
zyxelIfTable=_ZyxelIfTable_Object((1,3,6,1,4,1,890,1,15,3,27,1,3))
if mibBuilder.loadTexts:zyxelIfTable.setStatus(_A)
_ZyxelIfEntry_Object=MibTableRow
zyxelIfEntry=_ZyxelIfEntry_Object((1,3,6,1,4,1,890,1,15,3,27,1,3,1))
zyxelIfEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:zyxelIfEntry.setStatus(_A)
class _ZyIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('loopback',2)))
_ZyIfType_Type.__name__=_C
_ZyIfType_Object=MibTableColumn
zyIfType=_ZyIfType_Object((1,3,6,1,4,1,890,1,15,3,27,1,3,1,1),_ZyIfType_Type())
zyIfType.setMaxAccess(_G)
if mibBuilder.loadTexts:zyIfType.setStatus(_A)
_ZyIfId_Type=Integer32
_ZyIfId_Object=MibTableColumn
zyIfId=_ZyIfId_Object((1,3,6,1,4,1,890,1,15,3,27,1,3,1,2),_ZyIfId_Type())
zyIfId.setMaxAccess(_G)
if mibBuilder.loadTexts:zyIfId.setStatus(_A)
_ZyIfRowStatus_Type=RowStatus
_ZyIfRowStatus_Object=MibTableColumn
zyIfRowStatus=_ZyIfRowStatus_Object((1,3,6,1,4,1,890,1,15,3,27,1,3,1,3),_ZyIfRowStatus_Type())
zyIfRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelIf':zyxelIf,'zyxelIfSetup':zyxelIfSetup,'zyIfMaxNumberOfVlanIfs':zyIfMaxNumberOfVlanIfs,'zyIfMaxNumberOfLoopbackIfs':zyIfMaxNumberOfLoopbackIfs,'zyxelIfTable':zyxelIfTable,'zyxelIfEntry':zyxelIfEntry,_E:zyIfType,_F:zyIfId,'zyIfRowStatus':zyIfRowStatus})