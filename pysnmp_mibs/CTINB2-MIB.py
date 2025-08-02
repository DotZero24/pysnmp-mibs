_F='ctInbUtilDestSlot'
_E='ctInbUtilSrcSlot'
_D='Integer32'
_C='CTINB2-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctINBinfo2,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctINBinfo2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtInbUtil_ObjectIdentity=ObjectIdentity
ctInbUtil=_CtInbUtil_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,12,2,1))
class _CtInbUtilInterval_Type(Integer32):defaultValue=1
_CtInbUtilInterval_Type.__name__=_D
_CtInbUtilInterval_Object=MibScalar
ctInbUtilInterval=_CtInbUtilInterval_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,1),_CtInbUtilInterval_Type())
ctInbUtilInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctInbUtilInterval.setStatus(_A)
_CtInbUtilTable_Object=MibTable
ctInbUtilTable=_CtInbUtilTable_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2))
if mibBuilder.loadTexts:ctInbUtilTable.setStatus(_A)
_CtInbUtilEntry_Object=MibTableRow
ctInbUtilEntry=_CtInbUtilEntry_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1))
ctInbUtilEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:ctInbUtilEntry.setStatus(_A)
_CtInbUtilSrcSlot_Type=Integer32
_CtInbUtilSrcSlot_Object=MibTableColumn
ctInbUtilSrcSlot=_CtInbUtilSrcSlot_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,1),_CtInbUtilSrcSlot_Type())
ctInbUtilSrcSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilSrcSlot.setStatus(_A)
_CtInbUtilDestSlot_Type=Integer32
_CtInbUtilDestSlot_Object=MibTableColumn
ctInbUtilDestSlot=_CtInbUtilDestSlot_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,2),_CtInbUtilDestSlot_Type())
ctInbUtilDestSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilDestSlot.setStatus(_A)
_CtInbUtilHiByteCountA_Type=Integer32
_CtInbUtilHiByteCountA_Object=MibTableColumn
ctInbUtilHiByteCountA=_CtInbUtilHiByteCountA_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,3),_CtInbUtilHiByteCountA_Type())
ctInbUtilHiByteCountA.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilHiByteCountA.setStatus(_A)
_CtInbUtilLoByteCountA_Type=Integer32
_CtInbUtilLoByteCountA_Object=MibTableColumn
ctInbUtilLoByteCountA=_CtInbUtilLoByteCountA_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,4),_CtInbUtilLoByteCountA_Type())
ctInbUtilLoByteCountA.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilLoByteCountA.setStatus(_A)
_CtInbUtilHiByteCountB_Type=Integer32
_CtInbUtilHiByteCountB_Object=MibTableColumn
ctInbUtilHiByteCountB=_CtInbUtilHiByteCountB_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,5),_CtInbUtilHiByteCountB_Type())
ctInbUtilHiByteCountB.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilHiByteCountB.setStatus(_A)
_CtInbUtilLoByteCountB_Type=Integer32
_CtInbUtilLoByteCountB_Object=MibTableColumn
ctInbUtilLoByteCountB=_CtInbUtilLoByteCountB_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,6),_CtInbUtilLoByteCountB_Type())
ctInbUtilLoByteCountB.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilLoByteCountB.setStatus(_A)
_CtInbUtilAbsoluteA_Type=Integer32
_CtInbUtilAbsoluteA_Object=MibTableColumn
ctInbUtilAbsoluteA=_CtInbUtilAbsoluteA_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,7),_CtInbUtilAbsoluteA_Type())
ctInbUtilAbsoluteA.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilAbsoluteA.setStatus(_A)
_CtInbUtilAbsoluteB_Type=Integer32
_CtInbUtilAbsoluteB_Object=MibTableColumn
ctInbUtilAbsoluteB=_CtInbUtilAbsoluteB_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,8),_CtInbUtilAbsoluteB_Type())
ctInbUtilAbsoluteB.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilAbsoluteB.setStatus(_A)
_CtInbUtilAbsoluteTotal_Type=Integer32
_CtInbUtilAbsoluteTotal_Object=MibTableColumn
ctInbUtilAbsoluteTotal=_CtInbUtilAbsoluteTotal_Object((1,3,6,1,4,1,52,4,1,2,12,2,1,2,1,9),_CtInbUtilAbsoluteTotal_Type())
ctInbUtilAbsoluteTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ctInbUtilAbsoluteTotal.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctInbUtil':ctInbUtil,'ctInbUtilInterval':ctInbUtilInterval,'ctInbUtilTable':ctInbUtilTable,'ctInbUtilEntry':ctInbUtilEntry,_E:ctInbUtilSrcSlot,_F:ctInbUtilDestSlot,'ctInbUtilHiByteCountA':ctInbUtilHiByteCountA,'ctInbUtilLoByteCountA':ctInbUtilLoByteCountA,'ctInbUtilHiByteCountB':ctInbUtilHiByteCountB,'ctInbUtilLoByteCountB':ctInbUtilLoByteCountB,'ctInbUtilAbsoluteA':ctInbUtilAbsoluteA,'ctInbUtilAbsoluteB':ctInbUtilAbsoluteB,'ctInbUtilAbsoluteTotal':ctInbUtilAbsoluteTotal})