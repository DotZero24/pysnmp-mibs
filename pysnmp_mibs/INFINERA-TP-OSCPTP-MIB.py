_G='oscPtpGroup'
_F='oscPtpPmHistStatsEnable'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-OSCPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oscPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,36))
if mibBuilder.loadTexts:oscPtpMIB.setRevisions(('2012-10-20 00:00',))
_OscPtpTable_Object=MibTable
oscPtpTable=_OscPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,36,1))
if mibBuilder.loadTexts:oscPtpTable.setStatus(_A)
_OscPtpEntry_Object=MibTableRow
oscPtpEntry=_OscPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,36,1,1))
oscPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oscPtpEntry.setStatus(_A)
class _OscPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OscPtpPmHistStatsEnable_Type.__name__=_E
_OscPtpPmHistStatsEnable_Object=MibTableColumn
oscPtpPmHistStatsEnable=_OscPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,36,1,1,1),_OscPtpPmHistStatsEnable_Type())
oscPtpPmHistStatsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:oscPtpPmHistStatsEnable.setStatus(_A)
_OscPtpConformance_ObjectIdentity=ObjectIdentity
oscPtpConformance=_OscPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,36,3))
_OscPtpCompliances_ObjectIdentity=ObjectIdentity
oscPtpCompliances=_OscPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,36,3,1))
_OscPtpGroups_ObjectIdentity=ObjectIdentity
oscPtpGroups=_OscPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,36,3,2))
oscPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,36,3,2,1))
oscPtpGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:oscPtpGroup.setStatus(_A)
oscPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,36,3,1,1))
oscPtpCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:oscPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oscPtpMIB':oscPtpMIB,'oscPtpTable':oscPtpTable,'oscPtpEntry':oscPtpEntry,_F:oscPtpPmHistStatsEnable,'oscPtpConformance':oscPtpConformance,'oscPtpCompliances':oscPtpCompliances,'oscPtpCompliance':oscPtpCompliance,'oscPtpGroups':oscPtpGroups,_G:oscPtpGroup})