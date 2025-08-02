_I='otpGroup'
_H='otpProvSerialNumber'
_G='otpProvEqptType'
_F='otpMoId'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-OTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
otpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,39))
_OtpTable_Object=MibTable
otpTable=_OtpTable_Object((1,3,6,1,4,1,21296,2,2,2,1,39,1))
if mibBuilder.loadTexts:otpTable.setStatus(_A)
_OtpEntry_Object=MibTableRow
otpEntry=_OtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,39,1,1))
otpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:otpEntry.setStatus(_A)
_OtpMoId_Type=DisplayString
_OtpMoId_Object=MibTableColumn
otpMoId=_OtpMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,39,1,1,1),_OtpMoId_Type())
otpMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:otpMoId.setStatus(_A)
_OtpProvEqptType_Type=InfnEqptType
_OtpProvEqptType_Object=MibTableColumn
otpProvEqptType=_OtpProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,39,1,1,2),_OtpProvEqptType_Type())
otpProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:otpProvEqptType.setStatus(_A)
_OtpProvSerialNumber_Type=DisplayString
_OtpProvSerialNumber_Object=MibTableColumn
otpProvSerialNumber=_OtpProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,39,1,1,3),_OtpProvSerialNumber_Type())
otpProvSerialNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:otpProvSerialNumber.setStatus(_A)
_OtpConformance_ObjectIdentity=ObjectIdentity
otpConformance=_OtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,39,3))
_OtpCompliances_ObjectIdentity=ObjectIdentity
otpCompliances=_OtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,39,3,1))
_OtpGroups_ObjectIdentity=ObjectIdentity
otpGroups=_OtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,39,3,2))
otpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,39,3,2,1))
otpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:otpGroup.setStatus(_A)
otpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,39,3,1,1))
otpCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:otpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otpMIB':otpMIB,'otpTable':otpTable,'otpEntry':otpEntry,_F:otpMoId,_G:otpProvEqptType,_H:otpProvSerialNumber,'otpConformance':otpConformance,'otpCompliances':otpCompliances,'otpCompliance':otpCompliance,'otpGroups':otpGroups,_I:otpGroup})