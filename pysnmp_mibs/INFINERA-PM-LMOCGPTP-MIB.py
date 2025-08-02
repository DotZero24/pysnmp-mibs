_P='lmOcgPtpPmRealGroup'
_O='lmOcgPtpPmRealLmOcgSoPmd'
_N='lmOcgPtpPmRealLmOcgPmd'
_M='lmOcgPtpPmRealLmOcgRxEdfaLbc'
_L='lmOcgPtpPmRealLmOcgRxEdfaOpt'
_K='lmOcgPtpPmRealLmOcgRxEdfaOpr'
_J='lmOcgPtpPmRealLmOcgTxEdfaLbc'
_I='lmOcgPtpPmRealLmOcgTxEdfaOpt'
_H='lmOcgPtpPmRealLmOcgTxEdfaOpr'
_G='lmOcgPtpPmRealLmOcgOpr'
_F='lmOcgPtpPmRealLmOcgOpt'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-LMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lmOcgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,32))
if mibBuilder.loadTexts:lmOcgPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_LmOcgPtpPmRealTable_Object=MibTable
lmOcgPtpPmRealTable=_LmOcgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1))
if mibBuilder.loadTexts:lmOcgPtpPmRealTable.setStatus(_A)
_LmOcgPtpPmRealEntry_Object=MibTableRow
lmOcgPtpPmRealEntry=_LmOcgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1))
lmOcgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:lmOcgPtpPmRealEntry.setStatus(_A)
_LmOcgPtpPmRealLmOcgOpt_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgOpt_Object=MibTableColumn
lmOcgPtpPmRealLmOcgOpt=_LmOcgPtpPmRealLmOcgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,1),_LmOcgPtpPmRealLmOcgOpt_Type())
lmOcgPtpPmRealLmOcgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgOpt.setStatus(_A)
_LmOcgPtpPmRealLmOcgOpr_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgOpr_Object=MibTableColumn
lmOcgPtpPmRealLmOcgOpr=_LmOcgPtpPmRealLmOcgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,2),_LmOcgPtpPmRealLmOcgOpr_Type())
lmOcgPtpPmRealLmOcgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgOpr.setStatus(_A)
_LmOcgPtpPmRealLmOcgTxEdfaOpr_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgTxEdfaOpr_Object=MibTableColumn
lmOcgPtpPmRealLmOcgTxEdfaOpr=_LmOcgPtpPmRealLmOcgTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,3),_LmOcgPtpPmRealLmOcgTxEdfaOpr_Type())
lmOcgPtpPmRealLmOcgTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgTxEdfaOpr.setStatus(_A)
_LmOcgPtpPmRealLmOcgTxEdfaOpt_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgTxEdfaOpt_Object=MibTableColumn
lmOcgPtpPmRealLmOcgTxEdfaOpt=_LmOcgPtpPmRealLmOcgTxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,4),_LmOcgPtpPmRealLmOcgTxEdfaOpt_Type())
lmOcgPtpPmRealLmOcgTxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgTxEdfaOpt.setStatus(_A)
_LmOcgPtpPmRealLmOcgTxEdfaLbc_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgTxEdfaLbc_Object=MibTableColumn
lmOcgPtpPmRealLmOcgTxEdfaLbc=_LmOcgPtpPmRealLmOcgTxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,5),_LmOcgPtpPmRealLmOcgTxEdfaLbc_Type())
lmOcgPtpPmRealLmOcgTxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgTxEdfaLbc.setStatus(_A)
_LmOcgPtpPmRealLmOcgRxEdfaOpr_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgRxEdfaOpr_Object=MibTableColumn
lmOcgPtpPmRealLmOcgRxEdfaOpr=_LmOcgPtpPmRealLmOcgRxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,6),_LmOcgPtpPmRealLmOcgRxEdfaOpr_Type())
lmOcgPtpPmRealLmOcgRxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgRxEdfaOpr.setStatus(_A)
_LmOcgPtpPmRealLmOcgRxEdfaOpt_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgRxEdfaOpt_Object=MibTableColumn
lmOcgPtpPmRealLmOcgRxEdfaOpt=_LmOcgPtpPmRealLmOcgRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,7),_LmOcgPtpPmRealLmOcgRxEdfaOpt_Type())
lmOcgPtpPmRealLmOcgRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgRxEdfaOpt.setStatus(_A)
_LmOcgPtpPmRealLmOcgRxEdfaLbc_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgRxEdfaLbc_Object=MibTableColumn
lmOcgPtpPmRealLmOcgRxEdfaLbc=_LmOcgPtpPmRealLmOcgRxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,8),_LmOcgPtpPmRealLmOcgRxEdfaLbc_Type())
lmOcgPtpPmRealLmOcgRxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgRxEdfaLbc.setStatus(_A)
_LmOcgPtpPmRealLmOcgPmd_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgPmd_Object=MibTableColumn
lmOcgPtpPmRealLmOcgPmd=_LmOcgPtpPmRealLmOcgPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,9),_LmOcgPtpPmRealLmOcgPmd_Type())
lmOcgPtpPmRealLmOcgPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgPmd.setStatus(_A)
_LmOcgPtpPmRealLmOcgSoPmd_Type=FloatHundredths
_LmOcgPtpPmRealLmOcgSoPmd_Object=MibTableColumn
lmOcgPtpPmRealLmOcgSoPmd=_LmOcgPtpPmRealLmOcgSoPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,32,1,1,10),_LmOcgPtpPmRealLmOcgSoPmd_Type())
lmOcgPtpPmRealLmOcgSoPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpPmRealLmOcgSoPmd.setStatus(_A)
_LmOcgPtpPmConformance_ObjectIdentity=ObjectIdentity
lmOcgPtpPmConformance=_LmOcgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,32,3))
_LmOcgPtpPmCompliances_ObjectIdentity=ObjectIdentity
lmOcgPtpPmCompliances=_LmOcgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,32,3,1))
_LmOcgPtpPmGroups_ObjectIdentity=ObjectIdentity
lmOcgPtpPmGroups=_LmOcgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,32,3,2))
lmOcgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,32,3,2,1))
lmOcgPtpPmRealGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:lmOcgPtpPmRealGroup.setStatus(_A)
lmOcgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,32,3,1,1))
lmOcgPtpPmRealCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:lmOcgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lmOcgPtpPmMIB':lmOcgPtpPmMIB,'lmOcgPtpPmRealTable':lmOcgPtpPmRealTable,'lmOcgPtpPmRealEntry':lmOcgPtpPmRealEntry,_F:lmOcgPtpPmRealLmOcgOpt,_G:lmOcgPtpPmRealLmOcgOpr,_H:lmOcgPtpPmRealLmOcgTxEdfaOpr,_I:lmOcgPtpPmRealLmOcgTxEdfaOpt,_J:lmOcgPtpPmRealLmOcgTxEdfaLbc,_K:lmOcgPtpPmRealLmOcgRxEdfaOpr,_L:lmOcgPtpPmRealLmOcgRxEdfaOpt,_M:lmOcgPtpPmRealLmOcgRxEdfaLbc,_N:lmOcgPtpPmRealLmOcgPmd,_O:lmOcgPtpPmRealLmOcgSoPmd,'lmOcgPtpPmConformance':lmOcgPtpPmConformance,'lmOcgPtpPmCompliances':lmOcgPtpPmCompliances,'lmOcgPtpPmRealCompliance':lmOcgPtpPmRealCompliance,'lmOcgPtpPmGroups':lmOcgPtpPmGroups,_P:lmOcgPtpPmRealGroup})