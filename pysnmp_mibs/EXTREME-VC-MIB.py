_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
extremeVC=ModuleIdentity((1,3,6,1,4,1,1916,1,5))
_ExtremeVCLinkTable_Object=MibTable
extremeVCLinkTable=_ExtremeVCLinkTable_Object((1,3,6,1,4,1,1916,1,5,1))
if mibBuilder.loadTexts:extremeVCLinkTable.setStatus(_A)
_ExtremeVCLinkEntry_Object=MibTableRow
extremeVCLinkEntry=_ExtremeVCLinkEntry_Object((1,3,6,1,4,1,1916,1,5,1,1))
extremeVCLinkEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:extremeVCLinkEntry.setStatus(_A)
_ExtremeVCLinkValid_Type=TruthValue
_ExtremeVCLinkValid_Object=MibTableColumn
extremeVCLinkValid=_ExtremeVCLinkValid_Object((1,3,6,1,4,1,1916,1,5,1,1,1),_ExtremeVCLinkValid_Type())
extremeVCLinkValid.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVCLinkValid.setStatus(_A)
_ExtremeVCLinkDeviceId_Type=Integer32
_ExtremeVCLinkDeviceId_Object=MibTableColumn
extremeVCLinkDeviceId=_ExtremeVCLinkDeviceId_Object((1,3,6,1,4,1,1916,1,5,1,1,2),_ExtremeVCLinkDeviceId_Type())
extremeVCLinkDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVCLinkDeviceId.setStatus(_A)
_ExtremeVCLinkPortIndex_Type=Integer32
_ExtremeVCLinkPortIndex_Object=MibTableColumn
extremeVCLinkPortIndex=_ExtremeVCLinkPortIndex_Object((1,3,6,1,4,1,1916,1,5,1,1,3),_ExtremeVCLinkPortIndex_Type())
extremeVCLinkPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVCLinkPortIndex.setStatus(_A)
mibBuilder.exportSymbols('EXTREME-VC-MIB',**{'extremeVC':extremeVC,'extremeVCLinkTable':extremeVCLinkTable,'extremeVCLinkEntry':extremeVCLinkEntry,'extremeVCLinkValid':extremeVCLinkValid,'extremeVCLinkDeviceId':extremeVCLinkDeviceId,'extremeVCLinkPortIndex':extremeVCLinkPortIndex})