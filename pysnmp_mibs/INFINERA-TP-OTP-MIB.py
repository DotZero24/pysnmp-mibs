_F='optPtpGroup'
_E='optPtpProvNbrTP'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-OTP-MIB'
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
optPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,39))
if mibBuilder.loadTexts:optPtpMIB.setRevisions(('2013-10-20 00:00',))
_OptPtpTable_Object=MibTable
optPtpTable=_OptPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,39,1))
if mibBuilder.loadTexts:optPtpTable.setStatus(_A)
_OptPtpEntry_Object=MibTableRow
optPtpEntry=_OptPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,39,1,1))
optPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:optPtpEntry.setStatus(_A)
_OptPtpProvNbrTP_Type=DisplayString
_OptPtpProvNbrTP_Object=MibTableColumn
optPtpProvNbrTP=_OptPtpProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,39,1,1,1),_OptPtpProvNbrTP_Type())
optPtpProvNbrTP.setMaxAccess('read-write')
if mibBuilder.loadTexts:optPtpProvNbrTP.setStatus(_A)
_OptPtpConformance_ObjectIdentity=ObjectIdentity
optPtpConformance=_OptPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,39,3))
_OptPtpCompliances_ObjectIdentity=ObjectIdentity
optPtpCompliances=_OptPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,39,3,1))
_OptPtpGroups_ObjectIdentity=ObjectIdentity
optPtpGroups=_OptPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,39,3,2))
optPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,39,3,2,1))
optPtpGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:optPtpGroup.setStatus(_A)
optPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,39,3,1,1))
optPtpCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:optPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'optPtpMIB':optPtpMIB,'optPtpTable':optPtpTable,'optPtpEntry':optPtpEntry,_E:optPtpProvNbrTP,'optPtpConformance':optPtpConformance,'optPtpCompliances':optPtpCompliances,'optPtpCompliance':optPtpCompliance,'optPtpGroups':optPtpGroups,_F:optPtpGroup})