_I='expnPtpGroup'
_H='expnPtpMode'
_G='expnPtpExpectedNeighborPtp'
_F='expnPtpMoId'
_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-EXPNPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnExpnPtpMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnExpnPtpMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
expnPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,82))
if mibBuilder.loadTexts:expnPtpMIB.setRevisions(('2017-02-02 00:00',))
_ExpnPtpTable_Object=MibTable
expnPtpTable=_ExpnPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,82,1))
if mibBuilder.loadTexts:expnPtpTable.setStatus(_A)
_ExpnPtpEntry_Object=MibTableRow
expnPtpEntry=_ExpnPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,82,1,1))
expnPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:expnPtpEntry.setStatus(_A)
_ExpnPtpMoId_Type=DisplayString
_ExpnPtpMoId_Object=MibTableColumn
expnPtpMoId=_ExpnPtpMoId_Object((1,3,6,1,4,1,21296,2,2,2,2,82,1,1,1),_ExpnPtpMoId_Type())
expnPtpMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:expnPtpMoId.setStatus(_A)
_ExpnPtpExpectedNeighborPtp_Type=DisplayString
_ExpnPtpExpectedNeighborPtp_Object=MibTableColumn
expnPtpExpectedNeighborPtp=_ExpnPtpExpectedNeighborPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,82,1,1,2),_ExpnPtpExpectedNeighborPtp_Type())
expnPtpExpectedNeighborPtp.setMaxAccess(_E)
if mibBuilder.loadTexts:expnPtpExpectedNeighborPtp.setStatus(_A)
_ExpnPtpMode_Type=InfnExpnPtpMode
_ExpnPtpMode_Object=MibTableColumn
expnPtpMode=_ExpnPtpMode_Object((1,3,6,1,4,1,21296,2,2,2,2,82,1,1,3),_ExpnPtpMode_Type())
expnPtpMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:expnPtpMode.setStatus(_A)
_ExpnPtpConformance_ObjectIdentity=ObjectIdentity
expnPtpConformance=_ExpnPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,82,3))
_ExpnPtpCompliances_ObjectIdentity=ObjectIdentity
expnPtpCompliances=_ExpnPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,82,3,1))
_ExpnPtpGroups_ObjectIdentity=ObjectIdentity
expnPtpGroups=_ExpnPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,82,3,2))
expnPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,82,3,2,1))
expnPtpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:expnPtpGroup.setStatus(_A)
expnPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,82,3,1,1))
expnPtpCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:expnPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'expnPtpMIB':expnPtpMIB,'expnPtpTable':expnPtpTable,'expnPtpEntry':expnPtpEntry,_F:expnPtpMoId,_G:expnPtpExpectedNeighborPtp,_H:expnPtpMode,'expnPtpConformance':expnPtpConformance,'expnPtpCompliances':expnPtpCompliances,'expnPtpCompliance':expnPtpCompliance,'expnPtpGroups':expnPtpGroups,_I:expnPtpGroup})