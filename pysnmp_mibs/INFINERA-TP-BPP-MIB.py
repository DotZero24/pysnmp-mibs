_F='bppPtpGroup'
_E='bppPtpProvNbrTP'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-BPP-MIB'
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
bppPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,66))
if mibBuilder.loadTexts:bppPtpMIB.setRevisions(('2013-10-20 00:00',))
_BppPtpTable_Object=MibTable
bppPtpTable=_BppPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,66,1))
if mibBuilder.loadTexts:bppPtpTable.setStatus(_A)
_BppPtpEntry_Object=MibTableRow
bppPtpEntry=_BppPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,66,1,1))
bppPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bppPtpEntry.setStatus(_A)
_BppPtpProvNbrTP_Type=DisplayString
_BppPtpProvNbrTP_Object=MibTableColumn
bppPtpProvNbrTP=_BppPtpProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,66,1,1,1),_BppPtpProvNbrTP_Type())
bppPtpProvNbrTP.setMaxAccess('read-write')
if mibBuilder.loadTexts:bppPtpProvNbrTP.setStatus(_A)
_BppPtpConformance_ObjectIdentity=ObjectIdentity
bppPtpConformance=_BppPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,66,3))
_BppPtpCompliances_ObjectIdentity=ObjectIdentity
bppPtpCompliances=_BppPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,66,3,1))
_BppPtpGroups_ObjectIdentity=ObjectIdentity
bppPtpGroups=_BppPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,66,3,2))
bppPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,66,3,2,1))
bppPtpGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:bppPtpGroup.setStatus(_A)
bppPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,66,3,1,1))
bppPtpCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:bppPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bppPtpMIB':bppPtpMIB,'bppPtpTable':bppPtpTable,'bppPtpEntry':bppPtpEntry,_E:bppPtpProvNbrTP,'bppPtpConformance':bppPtpConformance,'bppPtpCompliances':bppPtpCompliances,'bppPtpCompliance':bppPtpCompliance,'bppPtpGroups':bppPtpGroups,_F:bppPtpGroup})