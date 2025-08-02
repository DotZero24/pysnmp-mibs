_J='snPortCARDirection'
_I='snPortCARifIndex'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='snPortCARRowIndex'
_C='FOUNDRY-CAR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
snCAR=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,16))
if mibBuilder.loadTexts:snCAR.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
class PacketSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('input',0),('output',1)))
class RateLimitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardAcc',1),('quickAcc',2),('all',3)))
class RateLimitAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('continue',1),('drop',2),('precedCont',3),('precedXmit',4),('xmit',5)))
_SnPortCARs_ObjectIdentity=ObjectIdentity
snPortCARs=_SnPortCARs_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,16,1))
_SnPortCARTable_Object=MibTable
snPortCARTable=_SnPortCARTable_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1))
if mibBuilder.loadTexts:snPortCARTable.setStatus(_A)
_SnPortCAREntry_Object=MibTableRow
snPortCAREntry=_SnPortCAREntry_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1))
snPortCAREntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_D))
if mibBuilder.loadTexts:snPortCAREntry.setStatus(_A)
_SnPortCARifIndex_Type=InterfaceIndex
_SnPortCARifIndex_Object=MibTableColumn
snPortCARifIndex=_SnPortCARifIndex_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,1),_SnPortCARifIndex_Type())
snPortCARifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARifIndex.setStatus(_A)
_SnPortCARDirection_Type=PacketSource
_SnPortCARDirection_Object=MibTableColumn
snPortCARDirection=_SnPortCARDirection_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,2),_SnPortCARDirection_Type())
snPortCARDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARDirection.setStatus(_A)
class _SnPortCARRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnPortCARRowIndex_Type.__name__=_H
_SnPortCARRowIndex_Object=MibTableColumn
snPortCARRowIndex=_SnPortCARRowIndex_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,3),_SnPortCARRowIndex_Type())
snPortCARRowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARRowIndex.setStatus(_A)
_SnPortCARType_Type=RateLimitType
_SnPortCARType_Object=MibTableColumn
snPortCARType=_SnPortCARType_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,4),_SnPortCARType_Type())
snPortCARType.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARType.setStatus(_A)
_SnPortCARAccIdx_Type=Integer32
_SnPortCARAccIdx_Object=MibTableColumn
snPortCARAccIdx=_SnPortCARAccIdx_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,5),_SnPortCARAccIdx_Type())
snPortCARAccIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARAccIdx.setStatus(_A)
_SnPortCARRate_Type=Integer32
_SnPortCARRate_Object=MibTableColumn
snPortCARRate=_SnPortCARRate_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,6),_SnPortCARRate_Type())
snPortCARRate.setMaxAccess(_E)
if mibBuilder.loadTexts:snPortCARRate.setStatus(_A)
_SnPortCARLimit_Type=Integer32
_SnPortCARLimit_Object=MibTableColumn
snPortCARLimit=_SnPortCARLimit_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,7),_SnPortCARLimit_Type())
snPortCARLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:snPortCARLimit.setStatus(_A)
_SnPortCARExtLimit_Type=Integer32
_SnPortCARExtLimit_Object=MibTableColumn
snPortCARExtLimit=_SnPortCARExtLimit_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,8),_SnPortCARExtLimit_Type())
snPortCARExtLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARExtLimit.setStatus(_A)
_SnPortCARConformAction_Type=RateLimitAction
_SnPortCARConformAction_Object=MibTableColumn
snPortCARConformAction=_SnPortCARConformAction_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,9),_SnPortCARConformAction_Type())
snPortCARConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARConformAction.setStatus(_A)
_SnPortCARExceedAction_Type=RateLimitAction
_SnPortCARExceedAction_Object=MibTableColumn
snPortCARExceedAction=_SnPortCARExceedAction_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,10),_SnPortCARExceedAction_Type())
snPortCARExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARExceedAction.setStatus(_A)
_SnPortCARStatSwitchedPkts_Type=Counter64
_SnPortCARStatSwitchedPkts_Object=MibTableColumn
snPortCARStatSwitchedPkts=_SnPortCARStatSwitchedPkts_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,11),_SnPortCARStatSwitchedPkts_Type())
snPortCARStatSwitchedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARStatSwitchedPkts.setStatus(_A)
_SnPortCARStatSwitchedBytes_Type=Counter64
_SnPortCARStatSwitchedBytes_Object=MibTableColumn
snPortCARStatSwitchedBytes=_SnPortCARStatSwitchedBytes_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,12),_SnPortCARStatSwitchedBytes_Type())
snPortCARStatSwitchedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARStatSwitchedBytes.setStatus(_A)
_SnPortCARStatFilteredPkts_Type=Counter64
_SnPortCARStatFilteredPkts_Object=MibTableColumn
snPortCARStatFilteredPkts=_SnPortCARStatFilteredPkts_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,13),_SnPortCARStatFilteredPkts_Type())
snPortCARStatFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARStatFilteredPkts.setStatus(_A)
_SnPortCARStatFilteredBytes_Type=Counter64
_SnPortCARStatFilteredBytes_Object=MibTableColumn
snPortCARStatFilteredBytes=_SnPortCARStatFilteredBytes_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,14),_SnPortCARStatFilteredBytes_Type())
snPortCARStatFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARStatFilteredBytes.setStatus(_A)
_SnPortCARStatCurBurst_Type=Gauge32
_SnPortCARStatCurBurst_Object=MibTableColumn
snPortCARStatCurBurst=_SnPortCARStatCurBurst_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,15),_SnPortCARStatCurBurst_Type())
snPortCARStatCurBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortCARStatCurBurst.setStatus(_A)
_SnPortCARRowStatus_Type=RowStatus
_SnPortCARRowStatus_Object=MibTableColumn
snPortCARRowStatus=_SnPortCARRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,16,1,1,1,16),_SnPortCARRowStatus_Type())
snPortCARRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snPortCARRowStatus.setStatus(_A)
_AgRateLimitCounterTable_Object=MibTable
agRateLimitCounterTable=_AgRateLimitCounterTable_Object((1,3,6,1,4,1,1991,1,1,3,16,1,2))
if mibBuilder.loadTexts:agRateLimitCounterTable.setStatus(_A)
_AgRateLimitCounterEntry_Object=MibTableRow
agRateLimitCounterEntry=_AgRateLimitCounterEntry_Object((1,3,6,1,4,1,1991,1,1,3,16,1,2,1))
agRateLimitCounterEntry.setIndexNames((0,_F,_G),(0,_C,_D))
if mibBuilder.loadTexts:agRateLimitCounterEntry.setStatus(_A)
_AgRateLimitCounterFwdedOctets_Type=Counter64
_AgRateLimitCounterFwdedOctets_Object=MibTableColumn
agRateLimitCounterFwdedOctets=_AgRateLimitCounterFwdedOctets_Object((1,3,6,1,4,1,1991,1,1,3,16,1,2,1,1),_AgRateLimitCounterFwdedOctets_Type())
agRateLimitCounterFwdedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:agRateLimitCounterFwdedOctets.setStatus(_A)
_AgRateLimitCounterDroppedOctets_Type=Counter64
_AgRateLimitCounterDroppedOctets_Object=MibTableColumn
agRateLimitCounterDroppedOctets=_AgRateLimitCounterDroppedOctets_Object((1,3,6,1,4,1,1991,1,1,3,16,1,2,1,2),_AgRateLimitCounterDroppedOctets_Type())
agRateLimitCounterDroppedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:agRateLimitCounterDroppedOctets.setStatus(_A)
_AgRateLimitCounterReMarkedOctets_Type=Counter64
_AgRateLimitCounterReMarkedOctets_Object=MibTableColumn
agRateLimitCounterReMarkedOctets=_AgRateLimitCounterReMarkedOctets_Object((1,3,6,1,4,1,1991,1,1,3,16,1,2,1,3),_AgRateLimitCounterReMarkedOctets_Type())
agRateLimitCounterReMarkedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:agRateLimitCounterReMarkedOctets.setStatus(_A)
_AgRateLimitCounterTotalOctets_Type=Counter64
_AgRateLimitCounterTotalOctets_Object=MibTableColumn
agRateLimitCounterTotalOctets=_AgRateLimitCounterTotalOctets_Object((1,3,6,1,4,1,1991,1,1,3,16,1,2,1,4),_AgRateLimitCounterTotalOctets_Type())
agRateLimitCounterTotalOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:agRateLimitCounterTotalOctets.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PacketSource':PacketSource,'RateLimitType':RateLimitType,'RateLimitAction':RateLimitAction,'snCAR':snCAR,'snPortCARs':snPortCARs,'snPortCARTable':snPortCARTable,'snPortCAREntry':snPortCAREntry,_I:snPortCARifIndex,_J:snPortCARDirection,_D:snPortCARRowIndex,'snPortCARType':snPortCARType,'snPortCARAccIdx':snPortCARAccIdx,'snPortCARRate':snPortCARRate,'snPortCARLimit':snPortCARLimit,'snPortCARExtLimit':snPortCARExtLimit,'snPortCARConformAction':snPortCARConformAction,'snPortCARExceedAction':snPortCARExceedAction,'snPortCARStatSwitchedPkts':snPortCARStatSwitchedPkts,'snPortCARStatSwitchedBytes':snPortCARStatSwitchedBytes,'snPortCARStatFilteredPkts':snPortCARStatFilteredPkts,'snPortCARStatFilteredBytes':snPortCARStatFilteredBytes,'snPortCARStatCurBurst':snPortCARStatCurBurst,'snPortCARRowStatus':snPortCARRowStatus,'agRateLimitCounterTable':agRateLimitCounterTable,'agRateLimitCounterEntry':agRateLimitCounterEntry,'agRateLimitCounterFwdedOctets':agRateLimitCounterFwdedOctets,'agRateLimitCounterDroppedOctets':agRateLimitCounterDroppedOctets,'agRateLimitCounterReMarkedOctets':agRateLimitCounterReMarkedOctets,'agRateLimitCounterTotalOctets':agRateLimitCounterTotalOctets})