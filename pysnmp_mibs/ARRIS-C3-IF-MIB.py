_D='dcxIfEntry'
_C='ARRIS-C3-IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cmtsC3IfMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,12))
_DcxIfObjects_ObjectIdentity=ObjectIdentity
dcxIfObjects=_DcxIfObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,12,1))
_DcxIfTable_Object=MibTable
dcxIfTable=_DcxIfTable_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1))
if mibBuilder.loadTexts:dcxIfTable.setStatus(_A)
_DcxIfEntry_Object=MibTableRow
dcxIfEntry=_DcxIfEntry_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1,1))
if mibBuilder.loadTexts:dcxIfEntry.setStatus(_A)
_DcxIfLoadInterval_Type=Unsigned32
_DcxIfLoadInterval_Object=MibTableColumn
dcxIfLoadInterval=_DcxIfLoadInterval_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1,1,1),_DcxIfLoadInterval_Type())
dcxIfLoadInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:dcxIfLoadInterval.setStatus(_A)
_DcxIfInputBitRate_Type=Unsigned32
_DcxIfInputBitRate_Object=MibTableColumn
dcxIfInputBitRate=_DcxIfInputBitRate_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1,1,2),_DcxIfInputBitRate_Type())
dcxIfInputBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxIfInputBitRate.setStatus(_A)
_DcxIfInputPacketRate_Type=Unsigned32
_DcxIfInputPacketRate_Object=MibTableColumn
dcxIfInputPacketRate=_DcxIfInputPacketRate_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1,1,3),_DcxIfInputPacketRate_Type())
dcxIfInputPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxIfInputPacketRate.setStatus(_A)
_DcxIfOutputBitRate_Type=Unsigned32
_DcxIfOutputBitRate_Object=MibTableColumn
dcxIfOutputBitRate=_DcxIfOutputBitRate_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1,1,4),_DcxIfOutputBitRate_Type())
dcxIfOutputBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxIfOutputBitRate.setStatus(_A)
_DcxIfOutputPacketRate_Type=Unsigned32
_DcxIfOutputPacketRate_Object=MibTableColumn
dcxIfOutputPacketRate=_DcxIfOutputPacketRate_Object((1,3,6,1,4,1,4115,1,4,3,12,1,1,1,5),_DcxIfOutputPacketRate_Type())
dcxIfOutputPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxIfOutputPacketRate.setStatus(_A)
ifEntry.registerAugmentions((_C,_D))
dcxIfEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'cmtsC3IfMIB':cmtsC3IfMIB,'dcxIfObjects':dcxIfObjects,'dcxIfTable':dcxIfTable,_D:dcxIfEntry,'dcxIfLoadInterval':dcxIfLoadInterval,'dcxIfInputBitRate':dcxIfInputBitRate,'dcxIfInputPacketRate':dcxIfInputPacketRate,'dcxIfOutputBitRate':dcxIfOutputBitRate,'dcxIfOutputPacketRate':dcxIfOutputPacketRate})