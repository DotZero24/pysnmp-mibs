_I='passivePtpGroup'
_H='passivePtpProvNbrTP'
_G='passivePtpType'
_F='passiveMoId'
_E='read-write'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-PASSIVE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
commonTerminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonTerminationPoint')
FloatHundredths,InfnEnableDisable=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnEnableDisable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
passivePtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,10,2))
if mibBuilder.loadTexts:passivePtpMIB.setRevisions(('2017-01-08 00:00',))
_PassivePtpTable_Object=MibTable
passivePtpTable=_PassivePtpTable_Object((1,3,6,1,4,1,21296,2,2,1,10,2,1))
if mibBuilder.loadTexts:passivePtpTable.setStatus(_A)
_PassivePtpEntry_Object=MibTableRow
passivePtpEntry=_PassivePtpEntry_Object((1,3,6,1,4,1,21296,2,2,1,10,2,1,1))
passivePtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:passivePtpEntry.setStatus(_A)
_PassiveMoId_Type=DisplayString
_PassiveMoId_Object=MibTableColumn
passiveMoId=_PassiveMoId_Object((1,3,6,1,4,1,21296,2,2,1,10,2,1,1,1),_PassiveMoId_Type())
passiveMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:passiveMoId.setStatus(_A)
_PassivePtpType_Type=DisplayString
_PassivePtpType_Object=MibTableColumn
passivePtpType=_PassivePtpType_Object((1,3,6,1,4,1,21296,2,2,1,10,2,1,1,2),_PassivePtpType_Type())
passivePtpType.setMaxAccess('read-only')
if mibBuilder.loadTexts:passivePtpType.setStatus(_A)
_PassivePtpProvNbrTP_Type=DisplayString
_PassivePtpProvNbrTP_Object=MibTableColumn
passivePtpProvNbrTP=_PassivePtpProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,1,10,2,1,1,3),_PassivePtpProvNbrTP_Type())
passivePtpProvNbrTP.setMaxAccess(_E)
if mibBuilder.loadTexts:passivePtpProvNbrTP.setStatus(_A)
_PassivePtpConformance_ObjectIdentity=ObjectIdentity
passivePtpConformance=_PassivePtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10,2,3))
_PassivePtpCompliances_ObjectIdentity=ObjectIdentity
passivePtpCompliances=_PassivePtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10,2,3,1))
_PassivePtpGroups_ObjectIdentity=ObjectIdentity
passivePtpGroups=_PassivePtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10,2,3,2))
passivePtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,10,2,3,2,1))
passivePtpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:passivePtpGroup.setStatus(_A)
passivePtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,10,2,3,1,1))
passivePtpCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:passivePtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'passivePtpMIB':passivePtpMIB,'passivePtpTable':passivePtpTable,'passivePtpEntry':passivePtpEntry,_F:passiveMoId,_G:passivePtpType,_H:passivePtpProvNbrTP,'passivePtpConformance':passivePtpConformance,'passivePtpCompliances':passivePtpCompliances,'passivePtpCompliance':passivePtpCompliance,'passivePtpGroups':passivePtpGroups,_I:passivePtpGroup})