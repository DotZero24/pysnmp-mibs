_F='fmpo25PtpGroup'
_E='fmpo25PtpProvNbrTP'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-FMPO25-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnEnableDisable=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnEnableDisable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fmpo25PtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,40))
if mibBuilder.loadTexts:fmpo25PtpMIB.setRevisions(('2013-10-20 00:00',))
_Fmpo25PtpTable_Object=MibTable
fmpo25PtpTable=_Fmpo25PtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,40,1))
if mibBuilder.loadTexts:fmpo25PtpTable.setStatus(_A)
_Fmpo25PtpEntry_Object=MibTableRow
fmpo25PtpEntry=_Fmpo25PtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,40,1,1))
fmpo25PtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fmpo25PtpEntry.setStatus(_A)
_Fmpo25PtpProvNbrTP_Type=DisplayString
_Fmpo25PtpProvNbrTP_Object=MibTableColumn
fmpo25PtpProvNbrTP=_Fmpo25PtpProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,40,1,1,1),_Fmpo25PtpProvNbrTP_Type())
fmpo25PtpProvNbrTP.setMaxAccess('read-write')
if mibBuilder.loadTexts:fmpo25PtpProvNbrTP.setStatus(_A)
_Fmpo25PtpConformance_ObjectIdentity=ObjectIdentity
fmpo25PtpConformance=_Fmpo25PtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,40,3))
_Fmpo25PtpCompliances_ObjectIdentity=ObjectIdentity
fmpo25PtpCompliances=_Fmpo25PtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,40,3,1))
_Fmpo25PtpGroups_ObjectIdentity=ObjectIdentity
fmpo25PtpGroups=_Fmpo25PtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,40,3,2))
fmpo25PtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,40,3,2,1))
fmpo25PtpGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:fmpo25PtpGroup.setStatus(_A)
fmpo25PtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,40,3,1,1))
fmpo25PtpCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:fmpo25PtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmpo25PtpMIB':fmpo25PtpMIB,'fmpo25PtpTable':fmpo25PtpTable,'fmpo25PtpEntry':fmpo25PtpEntry,_E:fmpo25PtpProvNbrTP,'fmpo25PtpConformance':fmpo25PtpConformance,'fmpo25PtpCompliances':fmpo25PtpCompliances,'fmpo25PtpCompliance':fmpo25PtpCompliance,'fmpo25PtpGroups':fmpo25PtpGroups,_F:fmpo25PtpGroup})