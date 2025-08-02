_F='rbpPtpGroup'
_E='rbpPtpProvNbrTP'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-RBP-MIB'
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
rbpPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,54))
if mibBuilder.loadTexts:rbpPtpMIB.setRevisions(('2013-10-20 00:00',))
_RbpPtpTable_Object=MibTable
rbpPtpTable=_RbpPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,54,1))
if mibBuilder.loadTexts:rbpPtpTable.setStatus(_A)
_RbpPtpEntry_Object=MibTableRow
rbpPtpEntry=_RbpPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,54,1,1))
rbpPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rbpPtpEntry.setStatus(_A)
_RbpPtpProvNbrTP_Type=DisplayString
_RbpPtpProvNbrTP_Object=MibTableColumn
rbpPtpProvNbrTP=_RbpPtpProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,54,1,1,1),_RbpPtpProvNbrTP_Type())
rbpPtpProvNbrTP.setMaxAccess('read-write')
if mibBuilder.loadTexts:rbpPtpProvNbrTP.setStatus(_A)
_RbpPtpConformance_ObjectIdentity=ObjectIdentity
rbpPtpConformance=_RbpPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,54,3))
_RbpPtpCompliances_ObjectIdentity=ObjectIdentity
rbpPtpCompliances=_RbpPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,54,3,1))
_RbpPtpGroups_ObjectIdentity=ObjectIdentity
rbpPtpGroups=_RbpPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,54,3,2))
rbpPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,54,3,2,1))
rbpPtpGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:rbpPtpGroup.setStatus(_A)
rbpPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,54,3,1,1))
rbpPtpCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:rbpPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbpPtpMIB':rbpPtpMIB,'rbpPtpTable':rbpPtpTable,'rbpPtpEntry':rbpPtpEntry,_E:rbpPtpProvNbrTP,'rbpPtpConformance':rbpPtpConformance,'rbpPtpCompliances':rbpPtpCompliances,'rbpPtpCompliance':rbpPtpCompliance,'rbpPtpGroups':rbpPtpGroups,_F:rbpPtpGroup})