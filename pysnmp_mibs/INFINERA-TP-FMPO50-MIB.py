_F='fmpo50PtpGroup'
_E='fmpo50PtpProvNbrTP'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-FMPO50-MIB'
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
fmpo50PtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,41))
if mibBuilder.loadTexts:fmpo50PtpMIB.setRevisions(('2013-10-20 00:00',))
_Fmpo50PtpTable_Object=MibTable
fmpo50PtpTable=_Fmpo50PtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,41,1))
if mibBuilder.loadTexts:fmpo50PtpTable.setStatus(_A)
_Fmpo50PtpEntry_Object=MibTableRow
fmpo50PtpEntry=_Fmpo50PtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,41,1,1))
fmpo50PtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fmpo50PtpEntry.setStatus(_A)
_Fmpo50PtpProvNbrTP_Type=DisplayString
_Fmpo50PtpProvNbrTP_Object=MibTableColumn
fmpo50PtpProvNbrTP=_Fmpo50PtpProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,41,1,1,1),_Fmpo50PtpProvNbrTP_Type())
fmpo50PtpProvNbrTP.setMaxAccess('read-write')
if mibBuilder.loadTexts:fmpo50PtpProvNbrTP.setStatus(_A)
_Fmpo50PtpConformance_ObjectIdentity=ObjectIdentity
fmpo50PtpConformance=_Fmpo50PtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,41,3))
_Fmpo50PtpCompliances_ObjectIdentity=ObjectIdentity
fmpo50PtpCompliances=_Fmpo50PtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,41,3,1))
_Fmpo50PtpGroups_ObjectIdentity=ObjectIdentity
fmpo50PtpGroups=_Fmpo50PtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,41,3,2))
fmpo50PtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,41,3,2,1))
fmpo50PtpGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:fmpo50PtpGroup.setStatus(_A)
fmpo50PtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,41,3,1,1))
fmpo50PtpCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:fmpo50PtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmpo50PtpMIB':fmpo50PtpMIB,'fmpo50PtpTable':fmpo50PtpTable,'fmpo50PtpEntry':fmpo50PtpEntry,_E:fmpo50PtpProvNbrTP,'fmpo50PtpConformance':fmpo50PtpConformance,'fmpo50PtpCompliances':fmpo50PtpCompliances,'fmpo50PtpCompliance':fmpo50PtpCompliance,'fmpo50PtpGroups':fmpo50PtpGroups,_F:fmpo50PtpGroup})