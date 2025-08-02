_H='dlmOcgPtpPmRealGroup'
_G='dlmOcgPtpPmRealDlmOcgOpr'
_F='dlmOcgPtpPmRealDlmOcgOpt'
_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-PM-DLMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlmOcgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,5))
if mibBuilder.loadTexts:dlmOcgPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_DlmOcgPtpPmRealTable_Object=MibTable
dlmOcgPtpPmRealTable=_DlmOcgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,5,1))
if mibBuilder.loadTexts:dlmOcgPtpPmRealTable.setStatus(_A)
_DlmOcgPtpPmRealEntry_Object=MibTableRow
dlmOcgPtpPmRealEntry=_DlmOcgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,5,1,1))
dlmOcgPtpPmRealEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dlmOcgPtpPmRealEntry.setStatus(_A)
_DlmOcgPtpPmRealDlmOcgOpt_Type=FloatHundredths
_DlmOcgPtpPmRealDlmOcgOpt_Object=MibTableColumn
dlmOcgPtpPmRealDlmOcgOpt=_DlmOcgPtpPmRealDlmOcgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,5,1,1,1),_DlmOcgPtpPmRealDlmOcgOpt_Type())
dlmOcgPtpPmRealDlmOcgOpt.setMaxAccess(_E)
if mibBuilder.loadTexts:dlmOcgPtpPmRealDlmOcgOpt.setStatus(_A)
_DlmOcgPtpPmRealDlmOcgOpr_Type=FloatHundredths
_DlmOcgPtpPmRealDlmOcgOpr_Object=MibTableColumn
dlmOcgPtpPmRealDlmOcgOpr=_DlmOcgPtpPmRealDlmOcgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,5,1,1,2),_DlmOcgPtpPmRealDlmOcgOpr_Type())
dlmOcgPtpPmRealDlmOcgOpr.setMaxAccess(_E)
if mibBuilder.loadTexts:dlmOcgPtpPmRealDlmOcgOpr.setStatus(_A)
_DlmOcgPtpPmConformance_ObjectIdentity=ObjectIdentity
dlmOcgPtpPmConformance=_DlmOcgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,5,3))
_DlmOcgPtpPmCompliances_ObjectIdentity=ObjectIdentity
dlmOcgPtpPmCompliances=_DlmOcgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,5,3,1))
_DlmOcgPtpPmGroups_ObjectIdentity=ObjectIdentity
dlmOcgPtpPmGroups=_DlmOcgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,5,3,2))
dlmOcgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,5,3,2,1))
dlmOcgPtpPmRealGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:dlmOcgPtpPmRealGroup.setStatus(_A)
dlmOcgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,5,3,1,1))
dlmOcgPtpPmRealCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:dlmOcgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlmOcgPtpPmMIB':dlmOcgPtpPmMIB,'dlmOcgPtpPmRealTable':dlmOcgPtpPmRealTable,'dlmOcgPtpPmRealEntry':dlmOcgPtpPmRealEntry,_F:dlmOcgPtpPmRealDlmOcgOpt,_G:dlmOcgPtpPmRealDlmOcgOpr,'dlmOcgPtpPmConformance':dlmOcgPtpPmConformance,'dlmOcgPtpPmCompliances':dlmOcgPtpPmCompliances,'dlmOcgPtpPmRealCompliance':dlmOcgPtpPmRealCompliance,'dlmOcgPtpPmGroups':dlmOcgPtpPmGroups,_H:dlmOcgPtpPmRealGroup})