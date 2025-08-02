_J='ampOtdrPtpGroup'
_I='ampOtdrPtpExpectedNeighborPtp'
_H='ampOtdrPtpLstSuccConnValidationTime'
_G='ampOtdrPtpConnectivityState'
_F='read-only'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-ampOtdrPtp-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ampOtdrPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,49))
if mibBuilder.loadTexts:ampOtdrPtpMIB.setRevisions(('2013-10-20 00:00',))
_AmpOtdrPtpTable_Object=MibTable
ampOtdrPtpTable=_AmpOtdrPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,49,1))
if mibBuilder.loadTexts:ampOtdrPtpTable.setStatus(_A)
_AmpOtdrPtpEntry_Object=MibTableRow
ampOtdrPtpEntry=_AmpOtdrPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,49,1,1))
ampOtdrPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ampOtdrPtpEntry.setStatus(_A)
class _AmpOtdrPtpConnectivityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notVerified',1),('valid',2),('inValid',3)))
_AmpOtdrPtpConnectivityState_Type.__name__=_E
_AmpOtdrPtpConnectivityState_Object=MibTableColumn
ampOtdrPtpConnectivityState=_AmpOtdrPtpConnectivityState_Object((1,3,6,1,4,1,21296,2,2,2,2,49,1,1,1),_AmpOtdrPtpConnectivityState_Type())
ampOtdrPtpConnectivityState.setMaxAccess(_F)
if mibBuilder.loadTexts:ampOtdrPtpConnectivityState.setStatus(_A)
_AmpOtdrPtpLstSuccConnValidationTime_Type=Integer32
_AmpOtdrPtpLstSuccConnValidationTime_Object=MibTableColumn
ampOtdrPtpLstSuccConnValidationTime=_AmpOtdrPtpLstSuccConnValidationTime_Object((1,3,6,1,4,1,21296,2,2,2,2,49,1,1,2),_AmpOtdrPtpLstSuccConnValidationTime_Type())
ampOtdrPtpLstSuccConnValidationTime.setMaxAccess(_F)
if mibBuilder.loadTexts:ampOtdrPtpLstSuccConnValidationTime.setStatus(_A)
_AmpOtdrPtpExpectedNeighborPtp_Type=DisplayString
_AmpOtdrPtpExpectedNeighborPtp_Object=MibTableColumn
ampOtdrPtpExpectedNeighborPtp=_AmpOtdrPtpExpectedNeighborPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,49,1,1,3),_AmpOtdrPtpExpectedNeighborPtp_Type())
ampOtdrPtpExpectedNeighborPtp.setMaxAccess('read-write')
if mibBuilder.loadTexts:ampOtdrPtpExpectedNeighborPtp.setStatus(_A)
_AmpOtdrPtpConformance_ObjectIdentity=ObjectIdentity
ampOtdrPtpConformance=_AmpOtdrPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,49,3))
_AmpOtdrPtpCompliances_ObjectIdentity=ObjectIdentity
ampOtdrPtpCompliances=_AmpOtdrPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,49,3,1))
_AmpOtdrPtpGroups_ObjectIdentity=ObjectIdentity
ampOtdrPtpGroups=_AmpOtdrPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,49,3,2))
ampOtdrPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,49,3,2,1))
ampOtdrPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ampOtdrPtpGroup.setStatus(_A)
ampOtdrPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,49,3,1,1))
ampOtdrPtpCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ampOtdrPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ampOtdrPtpMIB':ampOtdrPtpMIB,'ampOtdrPtpTable':ampOtdrPtpTable,'ampOtdrPtpEntry':ampOtdrPtpEntry,_G:ampOtdrPtpConnectivityState,_H:ampOtdrPtpLstSuccConnValidationTime,_I:ampOtdrPtpExpectedNeighborPtp,'ampOtdrPtpConformance':ampOtdrPtpConformance,'ampOtdrPtpCompliances':ampOtdrPtpCompliances,'ampOtdrPtpCompliance':ampOtdrPtpCompliance,'ampOtdrPtpGroups':ampOtdrPtpGroups,_J:ampOtdrPtpGroup})