_e='oscCtpPmRealGroup'
_d='oscCtpPmGroup'
_c='oscCtpPmRealOscXOverOPR'
_b='oscCtpPmRealOscRxPktsDropped'
_a='oscCtpPmRealOscRxPkts'
_Z='oscCtpPmRealOscRxBytes'
_Y='oscCtpPmRealOscTxPktsDropped'
_X='oscCtpPmRealOscTxPkts'
_W='oscCtpPmRealOscTxBytes'
_V='oscCtpPmRealOscOPR'
_U='oscCtpPmRealOscOPT'
_T='oscCtpPmRealOscLBC'
_S='oscCtpPmOscOPRAve'
_R='oscCtpPmOscOPRMax'
_Q='oscCtpPmOscOPRMin'
_P='oscCtpPmOscOPTAve'
_O='oscCtpPmOscOPTMax'
_N='oscCtpPmOscOPTMin'
_M='oscCtpPmOscLBCAve'
_L='oscCtpPmOscLBCMax'
_K='oscCtpPmOscLBCMin'
_J='oscCtpPmValidity'
_I='not-accessible'
_H='oscCtpPmTimestamp'
_G='oscCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OSCCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oscCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,10))
if mibBuilder.loadTexts:oscCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_OscCtpPmRealTable_Object=MibTable
oscCtpPmRealTable=_OscCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1))
if mibBuilder.loadTexts:oscCtpPmRealTable.setStatus(_A)
_OscCtpPmRealEntry_Object=MibTableRow
oscCtpPmRealEntry=_OscCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1))
oscCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oscCtpPmRealEntry.setStatus(_A)
_OscCtpPmRealOscLBC_Type=FloatHundredths
_OscCtpPmRealOscLBC_Object=MibTableColumn
oscCtpPmRealOscLBC=_OscCtpPmRealOscLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,1),_OscCtpPmRealOscLBC_Type())
oscCtpPmRealOscLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscLBC.setStatus(_A)
_OscCtpPmRealOscOPT_Type=FloatHundredths
_OscCtpPmRealOscOPT_Object=MibTableColumn
oscCtpPmRealOscOPT=_OscCtpPmRealOscOPT_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,2),_OscCtpPmRealOscOPT_Type())
oscCtpPmRealOscOPT.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscOPT.setStatus(_A)
_OscCtpPmRealOscOPR_Type=FloatHundredths
_OscCtpPmRealOscOPR_Object=MibTableColumn
oscCtpPmRealOscOPR=_OscCtpPmRealOscOPR_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,3),_OscCtpPmRealOscOPR_Type())
oscCtpPmRealOscOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscOPR.setStatus(_A)
_OscCtpPmRealOscTxBytes_Type=Counter64
_OscCtpPmRealOscTxBytes_Object=MibTableColumn
oscCtpPmRealOscTxBytes=_OscCtpPmRealOscTxBytes_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,4),_OscCtpPmRealOscTxBytes_Type())
oscCtpPmRealOscTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscTxBytes.setStatus(_A)
_OscCtpPmRealOscTxPkts_Type=Counter64
_OscCtpPmRealOscTxPkts_Object=MibTableColumn
oscCtpPmRealOscTxPkts=_OscCtpPmRealOscTxPkts_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,5),_OscCtpPmRealOscTxPkts_Type())
oscCtpPmRealOscTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscTxPkts.setStatus(_A)
_OscCtpPmRealOscTxPktsDropped_Type=Counter64
_OscCtpPmRealOscTxPktsDropped_Object=MibTableColumn
oscCtpPmRealOscTxPktsDropped=_OscCtpPmRealOscTxPktsDropped_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,6),_OscCtpPmRealOscTxPktsDropped_Type())
oscCtpPmRealOscTxPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscTxPktsDropped.setStatus(_A)
_OscCtpPmRealOscRxBytes_Type=Counter64
_OscCtpPmRealOscRxBytes_Object=MibTableColumn
oscCtpPmRealOscRxBytes=_OscCtpPmRealOscRxBytes_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,7),_OscCtpPmRealOscRxBytes_Type())
oscCtpPmRealOscRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscRxBytes.setStatus(_A)
_OscCtpPmRealOscRxPkts_Type=Counter64
_OscCtpPmRealOscRxPkts_Object=MibTableColumn
oscCtpPmRealOscRxPkts=_OscCtpPmRealOscRxPkts_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,8),_OscCtpPmRealOscRxPkts_Type())
oscCtpPmRealOscRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscRxPkts.setStatus(_A)
_OscCtpPmRealOscRxPktsDropped_Type=Counter64
_OscCtpPmRealOscRxPktsDropped_Object=MibTableColumn
oscCtpPmRealOscRxPktsDropped=_OscCtpPmRealOscRxPktsDropped_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,9),_OscCtpPmRealOscRxPktsDropped_Type())
oscCtpPmRealOscRxPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscRxPktsDropped.setStatus(_A)
_OscCtpPmRealOscXOverOPR_Type=FloatHundredths
_OscCtpPmRealOscXOverOPR_Object=MibTableColumn
oscCtpPmRealOscXOverOPR=_OscCtpPmRealOscXOverOPR_Object((1,3,6,1,4,1,21296,2,2,2,3,10,1,1,10),_OscCtpPmRealOscXOverOPR_Type())
oscCtpPmRealOscXOverOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmRealOscXOverOPR.setStatus(_A)
_OscCtpPmTable_Object=MibTable
oscCtpPmTable=_OscCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2))
if mibBuilder.loadTexts:oscCtpPmTable.setStatus(_A)
_OscCtpPmEntry_Object=MibTableRow
oscCtpPmEntry=_OscCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1))
oscCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:oscCtpPmEntry.setStatus(_A)
class _OscCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OscCtpPmTimestamp_Type.__name__=_F
_OscCtpPmTimestamp_Object=MibTableColumn
oscCtpPmTimestamp=_OscCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,1),_OscCtpPmTimestamp_Type())
oscCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:oscCtpPmTimestamp.setStatus(_A)
class _OscCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OscCtpPmSampleDuration_Type.__name__=_F
_OscCtpPmSampleDuration_Object=MibTableColumn
oscCtpPmSampleDuration=_OscCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,2),_OscCtpPmSampleDuration_Type())
oscCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:oscCtpPmSampleDuration.setStatus(_A)
_OscCtpPmValidity_Type=TruthValue
_OscCtpPmValidity_Object=MibTableColumn
oscCtpPmValidity=_OscCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,3),_OscCtpPmValidity_Type())
oscCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmValidity.setStatus(_A)
_OscCtpPmOscLBCMin_Type=FloatHundredths
_OscCtpPmOscLBCMin_Object=MibTableColumn
oscCtpPmOscLBCMin=_OscCtpPmOscLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,4),_OscCtpPmOscLBCMin_Type())
oscCtpPmOscLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscLBCMin.setStatus(_A)
_OscCtpPmOscLBCMax_Type=FloatHundredths
_OscCtpPmOscLBCMax_Object=MibTableColumn
oscCtpPmOscLBCMax=_OscCtpPmOscLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,5),_OscCtpPmOscLBCMax_Type())
oscCtpPmOscLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscLBCMax.setStatus(_A)
_OscCtpPmOscLBCAve_Type=FloatHundredths
_OscCtpPmOscLBCAve_Object=MibTableColumn
oscCtpPmOscLBCAve=_OscCtpPmOscLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,6),_OscCtpPmOscLBCAve_Type())
oscCtpPmOscLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscLBCAve.setStatus(_A)
_OscCtpPmOscOPTMin_Type=FloatHundredths
_OscCtpPmOscOPTMin_Object=MibTableColumn
oscCtpPmOscOPTMin=_OscCtpPmOscOPTMin_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,7),_OscCtpPmOscOPTMin_Type())
oscCtpPmOscOPTMin.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscOPTMin.setStatus(_A)
_OscCtpPmOscOPTMax_Type=FloatHundredths
_OscCtpPmOscOPTMax_Object=MibTableColumn
oscCtpPmOscOPTMax=_OscCtpPmOscOPTMax_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,8),_OscCtpPmOscOPTMax_Type())
oscCtpPmOscOPTMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscOPTMax.setStatus(_A)
_OscCtpPmOscOPTAve_Type=FloatHundredths
_OscCtpPmOscOPTAve_Object=MibTableColumn
oscCtpPmOscOPTAve=_OscCtpPmOscOPTAve_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,9),_OscCtpPmOscOPTAve_Type())
oscCtpPmOscOPTAve.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscOPTAve.setStatus(_A)
_OscCtpPmOscOPRMin_Type=FloatHundredths
_OscCtpPmOscOPRMin_Object=MibTableColumn
oscCtpPmOscOPRMin=_OscCtpPmOscOPRMin_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,10),_OscCtpPmOscOPRMin_Type())
oscCtpPmOscOPRMin.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscOPRMin.setStatus(_A)
_OscCtpPmOscOPRMax_Type=FloatHundredths
_OscCtpPmOscOPRMax_Object=MibTableColumn
oscCtpPmOscOPRMax=_OscCtpPmOscOPRMax_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,11),_OscCtpPmOscOPRMax_Type())
oscCtpPmOscOPRMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscOPRMax.setStatus(_A)
_OscCtpPmOscOPRAve_Type=FloatHundredths
_OscCtpPmOscOPRAve_Object=MibTableColumn
oscCtpPmOscOPRAve=_OscCtpPmOscOPRAve_Object((1,3,6,1,4,1,21296,2,2,2,3,10,2,1,12),_OscCtpPmOscOPRAve_Type())
oscCtpPmOscOPRAve.setMaxAccess(_C)
if mibBuilder.loadTexts:oscCtpPmOscOPRAve.setStatus(_A)
_OscCtpPmConformance_ObjectIdentity=ObjectIdentity
oscCtpPmConformance=_OscCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,10,3))
_OscCtpPmCompliances_ObjectIdentity=ObjectIdentity
oscCtpPmCompliances=_OscCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,10,3,1))
_OscCtpPmGroups_ObjectIdentity=ObjectIdentity
oscCtpPmGroups=_OscCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,10,3,2))
oscCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,10,3,2,1))
oscCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:oscCtpPmGroup.setStatus(_A)
oscCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,10,3,2,2))
oscCtpPmRealGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:oscCtpPmRealGroup.setStatus(_A)
oscCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,10,3,1,1))
oscCtpPmCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:oscCtpPmCompliance.setStatus(_A)
oscCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,10,3,1,2))
oscCtpPmRealCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:oscCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oscCtpPmMIB':oscCtpPmMIB,'oscCtpPmRealTable':oscCtpPmRealTable,'oscCtpPmRealEntry':oscCtpPmRealEntry,_T:oscCtpPmRealOscLBC,_U:oscCtpPmRealOscOPT,_V:oscCtpPmRealOscOPR,_W:oscCtpPmRealOscTxBytes,_X:oscCtpPmRealOscTxPkts,_Y:oscCtpPmRealOscTxPktsDropped,_Z:oscCtpPmRealOscRxBytes,_a:oscCtpPmRealOscRxPkts,_b:oscCtpPmRealOscRxPktsDropped,_c:oscCtpPmRealOscXOverOPR,'oscCtpPmTable':oscCtpPmTable,'oscCtpPmEntry':oscCtpPmEntry,_H:oscCtpPmTimestamp,_G:oscCtpPmSampleDuration,_J:oscCtpPmValidity,_K:oscCtpPmOscLBCMin,_L:oscCtpPmOscLBCMax,_M:oscCtpPmOscLBCAve,_N:oscCtpPmOscOPTMin,_O:oscCtpPmOscOPTMax,_P:oscCtpPmOscOPTAve,_Q:oscCtpPmOscOPRMin,_R:oscCtpPmOscOPRMax,_S:oscCtpPmOscOPRAve,'oscCtpPmConformance':oscCtpPmConformance,'oscCtpPmCompliances':oscCtpPmCompliances,'oscCtpPmCompliance':oscCtpPmCompliance,'oscCtpPmRealCompliance':oscCtpPmRealCompliance,'oscCtpPmGroups':oscCtpPmGroups,_d:oscCtpPmGroup,_e:oscCtpPmRealGroup})