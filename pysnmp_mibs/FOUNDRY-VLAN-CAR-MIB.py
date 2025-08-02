_G='snVLanCARRowIndex'
_F='snVLanCARDirection'
_E='snVLanCARVLanId'
_D='Integer32'
_C='FOUNDRY-VLAN-CAR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PacketSource,RateLimitAction,RateLimitType=mibBuilder.importSymbols('FOUNDRY-CAR-MIB','PacketSource','RateLimitAction','RateLimitType')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snVLanCAR=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,17))
if mibBuilder.loadTexts:snVLanCAR.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
_SnVLanCARs_ObjectIdentity=ObjectIdentity
snVLanCARs=_SnVLanCARs_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,17,1))
_SnVLanCARTable_Object=MibTable
snVLanCARTable=_SnVLanCARTable_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1))
if mibBuilder.loadTexts:snVLanCARTable.setStatus(_A)
_SnVLanCAREntry_Object=MibTableRow
snVLanCAREntry=_SnVLanCAREntry_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1))
snVLanCAREntry.setIndexNames((0,_C,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:snVLanCAREntry.setStatus(_A)
class _SnVLanCARVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanCARVLanId_Type.__name__=_D
_SnVLanCARVLanId_Object=MibTableColumn
snVLanCARVLanId=_SnVLanCARVLanId_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,1),_SnVLanCARVLanId_Type())
snVLanCARVLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARVLanId.setStatus(_A)
_SnVLanCARDirection_Type=PacketSource
_SnVLanCARDirection_Object=MibTableColumn
snVLanCARDirection=_SnVLanCARDirection_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,2),_SnVLanCARDirection_Type())
snVLanCARDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARDirection.setStatus(_A)
class _SnVLanCARRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnVLanCARRowIndex_Type.__name__=_D
_SnVLanCARRowIndex_Object=MibTableColumn
snVLanCARRowIndex=_SnVLanCARRowIndex_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,3),_SnVLanCARRowIndex_Type())
snVLanCARRowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARRowIndex.setStatus(_A)
_SnVLanCARType_Type=RateLimitType
_SnVLanCARType_Object=MibTableColumn
snVLanCARType=_SnVLanCARType_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,4),_SnVLanCARType_Type())
snVLanCARType.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARType.setStatus(_A)
_SnVLanCARAccIdx_Type=Integer32
_SnVLanCARAccIdx_Object=MibTableColumn
snVLanCARAccIdx=_SnVLanCARAccIdx_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,5),_SnVLanCARAccIdx_Type())
snVLanCARAccIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARAccIdx.setStatus(_A)
_SnVLanCARRate_Type=Integer32
_SnVLanCARRate_Object=MibTableColumn
snVLanCARRate=_SnVLanCARRate_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,6),_SnVLanCARRate_Type())
snVLanCARRate.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARRate.setStatus(_A)
_SnVLanCARLimit_Type=Integer32
_SnVLanCARLimit_Object=MibTableColumn
snVLanCARLimit=_SnVLanCARLimit_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,7),_SnVLanCARLimit_Type())
snVLanCARLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARLimit.setStatus(_A)
_SnVLanCARExtLimit_Type=Integer32
_SnVLanCARExtLimit_Object=MibTableColumn
snVLanCARExtLimit=_SnVLanCARExtLimit_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,8),_SnVLanCARExtLimit_Type())
snVLanCARExtLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARExtLimit.setStatus(_A)
_SnVLanCARConformAction_Type=RateLimitAction
_SnVLanCARConformAction_Object=MibTableColumn
snVLanCARConformAction=_SnVLanCARConformAction_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,9),_SnVLanCARConformAction_Type())
snVLanCARConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARConformAction.setStatus(_A)
_SnVLanCARExceedAction_Type=RateLimitAction
_SnVLanCARExceedAction_Object=MibTableColumn
snVLanCARExceedAction=_SnVLanCARExceedAction_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,10),_SnVLanCARExceedAction_Type())
snVLanCARExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARExceedAction.setStatus(_A)
_SnVLanCARStatSwitchedPkts_Type=Counter64
_SnVLanCARStatSwitchedPkts_Object=MibTableColumn
snVLanCARStatSwitchedPkts=_SnVLanCARStatSwitchedPkts_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,11),_SnVLanCARStatSwitchedPkts_Type())
snVLanCARStatSwitchedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARStatSwitchedPkts.setStatus(_A)
_SnVLanCARStatSwitchedBytes_Type=Counter64
_SnVLanCARStatSwitchedBytes_Object=MibTableColumn
snVLanCARStatSwitchedBytes=_SnVLanCARStatSwitchedBytes_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,12),_SnVLanCARStatSwitchedBytes_Type())
snVLanCARStatSwitchedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARStatSwitchedBytes.setStatus(_A)
_SnVLanCARStatFilteredPkts_Type=Counter64
_SnVLanCARStatFilteredPkts_Object=MibTableColumn
snVLanCARStatFilteredPkts=_SnVLanCARStatFilteredPkts_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,13),_SnVLanCARStatFilteredPkts_Type())
snVLanCARStatFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARStatFilteredPkts.setStatus(_A)
_SnVLanCARStatFilteredBytes_Type=Counter64
_SnVLanCARStatFilteredBytes_Object=MibTableColumn
snVLanCARStatFilteredBytes=_SnVLanCARStatFilteredBytes_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,14),_SnVLanCARStatFilteredBytes_Type())
snVLanCARStatFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARStatFilteredBytes.setStatus(_A)
_SnVLanCARStatCurBurst_Type=Gauge32
_SnVLanCARStatCurBurst_Object=MibTableColumn
snVLanCARStatCurBurst=_SnVLanCARStatCurBurst_Object((1,3,6,1,4,1,1991,1,1,3,17,1,1,1,15),_SnVLanCARStatCurBurst_Type())
snVLanCARStatCurBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanCARStatCurBurst.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'snVLanCAR':snVLanCAR,'snVLanCARs':snVLanCARs,'snVLanCARTable':snVLanCARTable,'snVLanCAREntry':snVLanCAREntry,_E:snVLanCARVLanId,_F:snVLanCARDirection,_G:snVLanCARRowIndex,'snVLanCARType':snVLanCARType,'snVLanCARAccIdx':snVLanCARAccIdx,'snVLanCARRate':snVLanCARRate,'snVLanCARLimit':snVLanCARLimit,'snVLanCARExtLimit':snVLanCARExtLimit,'snVLanCARConformAction':snVLanCARConformAction,'snVLanCARExceedAction':snVLanCARExceedAction,'snVLanCARStatSwitchedPkts':snVLanCARStatSwitchedPkts,'snVLanCARStatSwitchedBytes':snVLanCARStatSwitchedBytes,'snVLanCARStatFilteredPkts':snVLanCARStatFilteredPkts,'snVLanCARStatFilteredBytes':snVLanCARStatFilteredBytes,'snVLanCARStatCurBurst':snVLanCARStatCurBurst})