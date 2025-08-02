_G='read-write'
_F='ctBroadcastCtlInterface'
_E='ctBroadcastCtlSlotID'
_D='CT-BROADCAST-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctBroadcast,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctBroadcast')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtBroadcastCtl_ObjectIdentity=ObjectIdentity
ctBroadcastCtl=_CtBroadcastCtl_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,13,1))
_CtBroadcastCtlTable_Object=MibTable
ctBroadcastCtlTable=_CtBroadcastCtlTable_Object((1,3,6,1,4,1,52,4,1,2,13,1,1))
if mibBuilder.loadTexts:ctBroadcastCtlTable.setStatus(_A)
_CtBroadcastCtlEntry_Object=MibTableRow
ctBroadcastCtlEntry=_CtBroadcastCtlEntry_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1))
ctBroadcastCtlEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:ctBroadcastCtlEntry.setStatus(_A)
_CtBroadcastCtlSlotID_Type=Integer32
_CtBroadcastCtlSlotID_Object=MibTableColumn
ctBroadcastCtlSlotID=_CtBroadcastCtlSlotID_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,1),_CtBroadcastCtlSlotID_Type())
ctBroadcastCtlSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBroadcastCtlSlotID.setStatus(_A)
_CtBroadcastCtlInterface_Type=Integer32
_CtBroadcastCtlInterface_Object=MibTableColumn
ctBroadcastCtlInterface=_CtBroadcastCtlInterface_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,2),_CtBroadcastCtlInterface_Type())
ctBroadcastCtlInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBroadcastCtlInterface.setStatus(_A)
_CtBroadcastTotalBroadcastFrames_Type=Counter32
_CtBroadcastTotalBroadcastFrames_Object=MibTableColumn
ctBroadcastTotalBroadcastFrames=_CtBroadcastTotalBroadcastFrames_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,3),_CtBroadcastTotalBroadcastFrames_Type())
ctBroadcastTotalBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBroadcastTotalBroadcastFrames.setStatus(_A)
_CtBroadcastPeakBroadcastRate_Type=Integer32
_CtBroadcastPeakBroadcastRate_Object=MibTableColumn
ctBroadcastPeakBroadcastRate=_CtBroadcastPeakBroadcastRate_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,4),_CtBroadcastPeakBroadcastRate_Type())
ctBroadcastPeakBroadcastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBroadcastPeakBroadcastRate.setStatus(_A)
_CtBroadcastPeakBroadcastRateTime_Type=TimeTicks
_CtBroadcastPeakBroadcastRateTime_Object=MibTableColumn
ctBroadcastPeakBroadcastRateTime=_CtBroadcastPeakBroadcastRateTime_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,5),_CtBroadcastPeakBroadcastRateTime_Type())
ctBroadcastPeakBroadcastRateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBroadcastPeakBroadcastRateTime.setStatus(_A)
class _CtBroadcastPeakBroadcastClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noClear',2)))
_CtBroadcastPeakBroadcastClear_Type.__name__=_C
_CtBroadcastPeakBroadcastClear_Object=MibTableColumn
ctBroadcastPeakBroadcastClear=_CtBroadcastPeakBroadcastClear_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,6),_CtBroadcastPeakBroadcastClear_Type())
ctBroadcastPeakBroadcastClear.setMaxAccess(_G)
if mibBuilder.loadTexts:ctBroadcastPeakBroadcastClear.setStatus(_A)
class _CtBroadcastDesiredBroadcastThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtBroadcastDesiredBroadcastThreshold_Type.__name__=_C
_CtBroadcastDesiredBroadcastThreshold_Object=MibTableColumn
ctBroadcastDesiredBroadcastThreshold=_CtBroadcastDesiredBroadcastThreshold_Object((1,3,6,1,4,1,52,4,1,2,13,1,1,1,7),_CtBroadcastDesiredBroadcastThreshold_Type())
ctBroadcastDesiredBroadcastThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:ctBroadcastDesiredBroadcastThreshold.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ctBroadcastCtl':ctBroadcastCtl,'ctBroadcastCtlTable':ctBroadcastCtlTable,'ctBroadcastCtlEntry':ctBroadcastCtlEntry,_E:ctBroadcastCtlSlotID,_F:ctBroadcastCtlInterface,'ctBroadcastTotalBroadcastFrames':ctBroadcastTotalBroadcastFrames,'ctBroadcastPeakBroadcastRate':ctBroadcastPeakBroadcastRate,'ctBroadcastPeakBroadcastRateTime':ctBroadcastPeakBroadcastRateTime,'ctBroadcastPeakBroadcastClear':ctBroadcastPeakBroadcastClear,'ctBroadcastDesiredBroadcastThreshold':ctBroadcastDesiredBroadcastThreshold})