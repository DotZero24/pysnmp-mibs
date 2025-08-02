_F='sysPCMUnit'
_E='sysPCMSlot'
_D='BIANCA-BRICK-MIBSYS-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Sys_ObjectIdentity=ObjectIdentity
sys=_Sys_ObjectIdentity((1,3,6,1,4,1,272,4,17))
_SysPCMTable_Object=MibTable
sysPCMTable=_SysPCMTable_Object((1,3,6,1,4,1,272,4,17,1))
if mibBuilder.loadTexts:sysPCMTable.setStatus(_A)
_SysPCMEntry_Object=MibTableRow
sysPCMEntry=_SysPCMEntry_Object((1,3,6,1,4,1,272,4,17,1,1))
sysPCMEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:sysPCMEntry.setStatus(_A)
class _SysPCMSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SysPCMSlot_Type.__name__=_B
_SysPCMSlot_Object=MibTableColumn
sysPCMSlot=_SysPCMSlot_Object((1,3,6,1,4,1,272,4,17,1,1,1),_SysPCMSlot_Type())
sysPCMSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPCMSlot.setStatus(_A)
class _SysPCMUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,31))
_SysPCMUnit_Type.__name__=_B
_SysPCMUnit_Object=MibTableColumn
sysPCMUnit=_SysPCMUnit_Object((1,3,6,1,4,1,272,4,17,1,1,2),_SysPCMUnit_Type())
sysPCMUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPCMUnit.setStatus(_A)
class _SysPCMClockStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ready',1),('not-ready',2)))
_SysPCMClockStatus_Type.__name__=_B
_SysPCMClockStatus_Object=MibTableColumn
sysPCMClockStatus=_SysPCMClockStatus_Object((1,3,6,1,4,1,272,4,17,1,1,3),_SysPCMClockStatus_Type())
sysPCMClockStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPCMClockStatus.setStatus(_A)
class _SysPCMClockMaster_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('candidate',1),('master',2)))
_SysPCMClockMaster_Type.__name__=_B
_SysPCMClockMaster_Object=MibTableColumn
sysPCMClockMaster=_SysPCMClockMaster_Object((1,3,6,1,4,1,272,4,17,1,1,4),_SysPCMClockMaster_Type())
sysPCMClockMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPCMClockMaster.setStatus(_A)
class _SysPCMMasterPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_SysPCMMasterPrio_Type.__name__=_B
_SysPCMMasterPrio_Object=MibTableColumn
sysPCMMasterPrio=_SysPCMMasterPrio_Object((1,3,6,1,4,1,272,4,17,1,1,5),_SysPCMMasterPrio_Type())
sysPCMMasterPrio.setMaxAccess('read-write')
if mibBuilder.loadTexts:sysPCMMasterPrio.setStatus(_A)
_SysPCMChanges_Type=Counter32
_SysPCMChanges_Object=MibTableColumn
sysPCMChanges=_SysPCMChanges_Object((1,3,6,1,4,1,272,4,17,1,1,10),_SysPCMChanges_Type())
sysPCMChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPCMChanges.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bintec':bintec,'bibo':bibo,'sys':sys,'sysPCMTable':sysPCMTable,'sysPCMEntry':sysPCMEntry,_E:sysPCMSlot,_F:sysPCMUnit,'sysPCMClockStatus':sysPCMClockStatus,'sysPCMClockMaster':sysPCMClockMaster,'sysPCMMasterPrio':sysPCMMasterPrio,'sysPCMChanges':sysPCMChanges})